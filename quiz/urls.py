from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .view_files.quiz_views import QuizViewSet
from .view_files.choice_views import ChoicesViewSet
from .view_files.question_views import QuestionViewSet
from .view_files.user_choices_views import UserChoicesViewSet
from .view_files.user_quiz_scores_views import UserQuizScoresViewSet


router = DefaultRouter()
router.register(r'quiz', QuizViewSet, basename="quiz")
router.register(r'choices', ChoicesViewSet, basename="choices")
router.register(r'question', QuestionViewSet, basename="question")
router.register(r'user_choices', UserChoicesViewSet, basename="user-choices")
router.register(r'user_quiz_scores', UserQuizScoresViewSet, basename="user-quiz-scores")

urlpatterns = [
    path('', include(router.urls)),
]