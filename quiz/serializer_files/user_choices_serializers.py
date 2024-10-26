# serializers.py
from rest_framework import serializers
from ..models import UserChoises

class UserChoisesCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChoises
        fields = '__all__'
        read_only_fields = [
            'user'
            , 'date_submited'
            , 'quiz'
            , 'is_correct'
            , 'is_submited'
            , 'question'
        ]
