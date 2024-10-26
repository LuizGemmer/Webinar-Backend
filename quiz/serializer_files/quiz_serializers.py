# serializers.py
from rest_framework import serializers
from ..models import Quiz

class QuizCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        read_only_fields = ['created_by', 'modified_by', 'date_created', 'last_modified_date']
