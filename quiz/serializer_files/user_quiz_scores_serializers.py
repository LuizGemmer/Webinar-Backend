# serializers.py

from django.utils import timezone

from rest_framework import serializers
from ..models import UserQuizScores, UserChoices, Choices

class UserQuizScoresCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuizScores
        fields = '__all__'
        read_only_fields = [
            'user'
        ]

class SubmitUserQuizScoreSerializer(serializers.ModelSerializer):
    """
    Serlializer responsible to submit the user atempt at the quiz, calculating its score
    """

    choices = serializers.ListField(
        child=serializers.CharField(max_length=255)
        , allow_empty=False
        , write_only=True
    )

    class Meta:
        model = UserQuizScores
        fields = ['id', 'quiz', 'is_submited', 'date_submited', 'score', 'choices', 'is_aproved']
        read_only_fields = ['id', 'quiz', 'is_submited', 'date_submited', 'score', 'is_aproved']

    def create(self, validated_data):
        # Set the quiz score as submited
        date_submited = timezone.now()

        instance = UserQuizScores(
            user = self.context['request'].user
            , quiz = self.context['quiz']
        )
        instance.save()

        # Calculate the quiz score
        self.submit_choices(instance, date_submited, validated_data)

        instance.score = instance.calculate_score()
        instance.is_submited = True
        instance.date_submited = date_submited
        instance.is_aproved = instance.quiz_score_above_required_score()

        instance.save()
        # Proceds to save the instance normally
        return instance

    def submit_choices(self, instance, date, validated_data):
        """
        Set all choices as submited
        """
        for choice in validated_data['choices']:
            choice_obj = Choices.objects.get(id=choice)

            user_choice = UserChoices()
            user_choice.user = instance.user
            user_choice.choice = choice_obj
            user_choice.is_submited = True
            user_choice.date_submited = date
            user_choice.question = choice_obj.question
            user_choice.user_quiz = instance

            user_choice.save()