# serializers.py
from rest_framework import serializers
from ..models import Choices

class ChoicesCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = '__all__'
        read_only_fields = ['created_by', 'modified_by', 'date_created', 'last_modified_date']

class UserChoicesSerializer(serializers.ModelSerializer):
    """
    Serializes the choice model, sending only relevant data for the user.
    """
    class Meta:
        model = Choices
        fields = ['id', 'title']
