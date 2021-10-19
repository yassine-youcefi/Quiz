from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Quiz
from django.views.generic import ListView
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

