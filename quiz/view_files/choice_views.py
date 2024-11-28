# views.py
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from ..models import Choices
from ..serializer_files.choice_serializers import (
    ChoicesCRUDSerializer
    , UserChoicesSerializer
)

class ChoicesViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    queryset = Choices.objects.filter(is_active=True)
    serializer_class = ChoicesCRUDSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set created_by and modified_by on creation
        serializer.save(created_by=self.request.user, modified_by=self.request.user)

    def perform_update(self, serializer):
        # Update modified_by on update
        serializer.save(modified_by=self.request.user)

    def perform_destroy(self, instance):
        # Instead of deleting, set is_active to False (soft delete)
        instance.is_active = False
        instance.modified_by = self.request.user
        instance.save(update_fields=['is_active', 'modified_by'])

class GetChoicesByQuestion(generics.ListAPIView):
    # TODO change serializer for one with less information, currently sending the info if the choice is correct or not
    serializer_class = UserChoicesSerializer 

    def get_queryset(self):
        question_id = self.kwargs['id']
        return Choices.objects.filter(question_id=question_id).filter(is_active=True)