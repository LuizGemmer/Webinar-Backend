# serializers.py
from rest_framework import serializers
from ..models import UserChoices

class UserChoisesCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChoices
        fields = '__all__'
        read_only_fields = [
            'user'
            , 'date_submited'
            , 'quiz'
            , 'is_correct'
            , 'is_submited'
            , 'question'
        ]
