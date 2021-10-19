from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Quiz
from django.views.generic import ListView
from django.http import JsonResponse
# from rest_framework.views import APIView


def index(request):
    return render(request, 'templates/index.html')

class QuizzesList(ListView):
    model = Quiz
    template_name = 'templates/quizes.html'
 

def quiz_detail(request, pk):
    context = {
        'quiz': Quiz.objects.get(pk=pk)
    }
    return render(request, 'templates/quize_details.html', context)        


def quiz_data(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for question in quiz.get_questions():
        # questions.append(qu estion.text)
        answers = []
        for answer in question.get_answers():
            answers.append(answer.text)

        questions.append({str(question):answers})
    return JsonResponse({
        'questions': questions,
        'time' : quiz.time,
        })