# serializers.py
from rest_framework import serializers
from ..models import Question

from .choice_serializers import UserChoicesSerializer
from ..models import UserQuizScores

class QuestionCRUDSerializer(serializers.ModelSerializer):
    choices_set = UserChoicesSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'quiz', 'is_active', 'choices_set']
        read_only_fields = ['created_by', 'modified_by', 'date_created', 'last_modified_date']