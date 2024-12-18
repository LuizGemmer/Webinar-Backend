# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import UserChoices
from ..serializer_files.user_choices_serializers import UserChoisesCRUDSerializer

class UserChoicesViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    queryset = UserChoices.objects.filter(is_active=True)
    serializer_class = UserChoisesCRUDSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set created_by and modified_by on creation
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save()


