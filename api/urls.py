from django.urls import path
from .views import (
    QuizListAPIView, QuizCreateAPIView, QuizDetailAPIView, QuizUpdateAPIView,
    QuestionListAPIView, QuestionCreateAPIView, QuestionDetailAPIView, QuestionUpdateAPIView,
    OptionListAPIView, OptionCreateAPIView, OptionDetailAPIView, OptionUpdateAPIView
)

urlpatterns = [
    path('quizzes/', QuizListAPIView.as_view(), name='QuizSerializer'),
    path('quizzes/create/', QuizCreateAPIView.as_view(), name='QuizSerializer'),
    path('quizzes/<int:pk>/', QuizDetailAPIView.as_view(), name='QuizSerializer'),
    path('quizzes/<int:pk>/update/', QuizUpdateAPIView.as_view(), name='QuizSerializer'),

    path('quizzes/<int:quiz_id>/questions/', QuestionListAPIView.as_view(), name='QuestionSerializer'),
    path('questions/create/', QuestionCreateAPIView.as_view(), name='QuestionSerializer'),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='QuestionSerializer'),
    path('questions/<int:pk>/update/', QuestionUpdateAPIView.as_view(), name='QuestionSerializer'),

    path('questions/<int:question_id>/options/', OptionListAPIView.as_view(), name='OptionSerializer'),
    path('options/create/', OptionCreateAPIView.as_view(), name='OptionSerializer'),
    path('options/<int:pk>/', OptionDetailAPIView.as_view(), name='OptionSerializer'),
    path('options/<int:pk>/update/', OptionUpdateAPIView.as_view(), name='OptionSerializer'),
]
