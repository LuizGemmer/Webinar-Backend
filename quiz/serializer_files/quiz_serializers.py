# serializers.py
from rest_framework import serializers
from ..models import Quiz, UserQuizScores

class QuizCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        read_only_fields = ['created_by', 'modified_by', 'date_created', 'last_modified_date']

class QuizWithUserAtemptSerializar(serializers.ModelSerializer):
    user_attempt = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ["id","name","description","required_grade","is_active","related_class", 'user_attempt']
        read_only_fields = fields

    def get_user_attempt(self, obj):
        user = self.context['request'].user
        
        user_attempt = UserQuizScores.objects.filter(
            user=user, quiz=obj, date_submited__isnull=False
        ).order_by('-date_submited').first()

        user_attempt_data = {
            'date_submited': None,
            'score': None,
            'is_submited': None,
            'is_aproved': None
        }

        if user_attempt.date_submited != None:
            user_attempt_data['date_submited'] = user_attempt.date_submited
            user_attempt_data['is_submited'] = user_attempt.is_submited
            user_attempt_data['is_aproved'] = user_attempt.is_aproved
            user_attempt_data['score'] = user_attempt.score

        return user_attempt_data