from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from connect.models import User
from main.models import Question, Quiz

# _______________ / User views \_______________
class UserView(APIView):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = GetUserSerializer(user)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = PutUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# _______________ / Quiz views \_______________
class QuizListView(APIView):
    def get(self, request):
        quizzes = Quiz.objects.filter(admin=request.user.id)
        serializer = GetQuizListSerializer(quizzes, many=True)
        return Response(serializer.data)

class QuizView(APIView):
    def get(self, request, pk, format=None):
        quiz = Quiz.objects.get(pk=pk)
        serializer = GetQuizSerializer(quiz)
        return Response(serializer.data)

# _______________ / Questions views \_______________
class QuestionsListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = GetQuestionListSerializer(questions, many=True)
        return Response(serializer.data)

class QuestionsListQuizView(APIView):
    def get(self, request, pk, format=None):
        quiz = Quiz.objects.get(pk=pk, admin=request.user.id)
        questions = Question.objects.filter(quiz=quiz.id)
        serializer = GetQuestionListSerializer(questions, many=True)
        return Response(serializer.data)    

   
class QuestionView(APIView):
    def get(self, request, pk, format=None):
        question = Question.objects.get(pk=pk)
        serializer = GetQuestionSerializer(question)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        question = Question.objects.get(pk=pk)
        serializer = PutQuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)    

class QuestionCreateView(APIView):

    def post(self, request, format=None):
        serializer = PostQuestionSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.validated_data['admin'] = request.user.id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# _______________ / Answers views \_______________
class AnswersListView(APIView):
    def get(self, request, pk, format=None):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
        answers = Answer.objects.filter(question=question.id)
        serializer = AnswerListSerializer(answers, many=True)
        return Response(serializer.data)
    def post(self, request, pk, format=None):
        question = Question.objects.get(pk=pk)
        print(question)
        request.data['user'] = request.user.id
        request.data['question'] = question.id
        serializer = PostAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        
    def delete(self, request, pk, format=None):
        answer = Answer.objects.get(pk=pk)
        answer.delete()
        return Response(status=status.HTTP_201_CREATED)    