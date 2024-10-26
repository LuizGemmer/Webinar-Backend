# serializers.py
from rest_framework import serializers
from ..models import UserQuizScores

class UserQuizScoresCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuizScores
        fields = '__all__'
        read_only_fields = [
            'user'
        ]
