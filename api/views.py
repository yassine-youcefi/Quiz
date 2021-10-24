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



# _______________ / Questions views \_______________
class QuestionsListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = GetQuestionListSerializer(questions)
        return Response(serializer.data)