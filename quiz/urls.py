from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .view_files.quiz_views import QuizViewSet, GetQuizesByRelatedClassID
from .view_files.choice_views import ChoicesViewSet, GetChoicesByQuestion
from .view_files.question_views import QuestionViewSet, GetQuestionsByQuiz
from .view_files.user_choices_views import UserChoicesViewSet
from .view_files.user_quiz_scores_views import UserQuizScoresViewSet, SubmitUserQuizScoreView


router = DefaultRouter()
router.register(r'quiz', QuizViewSet, basename="quiz")
router.register(r'choices', ChoicesViewSet, basename="choices")
router.register(r'question', QuestionViewSet, basename="question")
router.register(r'user_choices', UserChoicesViewSet, basename="user-choices")
router.register(r'user_quiz_scores', UserQuizScoresViewSet, basename="user-quiz-scores")

urlpatterns = [
    path('', include(router.urls)),
    
    path('question/by_quiz_id/<uuid:id>/', GetQuestionsByQuiz.as_view(), name='question-by-quiz'),
    
    path('quiz/get_quizes_by_function_id/<uuid:id>/', GetQuizesByRelatedClassID.as_view(), name='get-quizes-by-function-id'),

    path('choices/by_question_id/<uuid:id>/', GetChoicesByQuestion.as_view(), name='choices-by-question'),

    path('user_quiz_scores/submit/<uuid:id>/', SubmitUserQuizScoreView.as_view(), name='user-quiz-scores-submit'),
]