# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Choices
from ..serializer_files.choice_serializers import ChoicesCRUDSerializer

class ChoicesViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    queryset = Choices.objects.all()
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