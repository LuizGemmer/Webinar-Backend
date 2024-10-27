# serializers.py

from django.utils import timezone

from rest_framework import serializers
from ..models import UserQuizScores

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
    class Meta:
        model = UserQuizScores
        fields = ['id', 'quiz', 'is_submited', 'date_submited', 'score']
        read_only_fields = fields

    def update(self, instance, validated_data):
        # Set the quiz score as submited
        date_submited = timezone.now()
        instance.is_submited = True
        instance.date_submited = date_submited

        # Calculate the quiz score
        instance.score = instance.calculate_score()
        
        self.submit_choices(instance, date_submited)

        # Proceds to save the instance normally
        return super().update(instance, validated_data)

    def submit_choices(self, instance, date):
        """
        Set all choices as submited
        """
        user_choice_set = instance.userchoices_set.all()
        for choice in user_choice_set:
            choice.is_submited = True
            choice.date_submited = date
            choice.save()