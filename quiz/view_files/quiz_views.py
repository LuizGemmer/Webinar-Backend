# views.py
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from ..models import Quiz
from ..serializer_files.quiz_serializers import QuizCRUDSerializer

class QuizViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    queryset = Quiz.objects.filter(is_active=True)
    serializer_class = QuizCRUDSerializer
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

class GetQuizesByRelatedClassID(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizCRUDSerializer
    
    def get_queryset(self):
        function_id = self.kwargs['id']
        return Quiz.objects.filter(related_class_id=function_id).filter(is_active=True)

