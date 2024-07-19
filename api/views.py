from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quiz, Question, Option
from .serializers import QuizSerializer, QuestionSerializer, OptionSerializer

class QuizListAPIView(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizCreateAPIView(CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizUpdateAPIView(UpdateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter(quiz_id=self.kwargs['quiz_id'])

class QuestionCreateAPIView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionUpdateAPIView(UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class OptionListAPIView(ListAPIView):
    serializer_class = OptionSerializer

    def get_queryset(self):
        return Option.objects.filter(question_id=self.kwargs['question_id'])

class OptionCreateAPIView(CreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class OptionDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class OptionUpdateAPIView(UpdateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
