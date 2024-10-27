# views.py
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from ..models import Question
from ..serializer_files.question_serializers import QuestionCRUDSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing quiz instances.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionCRUDSerializer
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

class GetQuestionsByQuiz(generics.ListAPIView):
    serializer_class = QuestionCRUDSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['id']
        return Question.objects.filter(quiz_id=quiz_id)