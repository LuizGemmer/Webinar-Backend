# views.py
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from ..models import UserQuizScores, Quiz
from ..serializer_files.user_quiz_scores_serializers import (
    UserQuizScoresCRUDSerializer
    , SubmitUserQuizScoreSerializer
)

class UserQuizScoresViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user quiz scores instances.
    """
    queryset = UserQuizScores.objects.filter(is_active=True)
    serializer_class = UserQuizScoresCRUDSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save()

class SubmitUserQuizScoreView(generics.CreateAPIView):
    """
    A view to submit the user quiz score.
    This view will set the user quiz score instace and related user choices to True,
    preventing further modifications to the data. The score will also be set. 
    """
    queryset = UserQuizScores.objects.filter(is_active=True)
    serializer_class = SubmitUserQuizScoreSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['quiz'] = Quiz.objects.get(id=self.kwargs.get('id'))
        return context
