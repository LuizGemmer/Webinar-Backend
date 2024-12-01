# serializers.py
from rest_framework import serializers
from ..models import Choices, UserChoices

class ChoicesCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = '__all__'
        read_only_fields = ['created_by', 'modified_by', 'date_created', 'last_modified_date']

class UserChoicesSerializer(serializers.ModelSerializer):
    """
    Serializes the choice model, sending only relevant data for the user.
    """
    was_chosen = serializers.SerializerMethodField()

    class Meta:
        model = Choices
        fields = ['id', 'title', 'is_correct', 'was_chosen']

    def get_was_chosen(self, obj):
        user = self.context['request'].user
        
        user_choice = UserChoices.objects.filter(
            user=user, choice=obj
        ).order_by('-date_submited').first()

        return True if user_choice else False
