from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Quiz
from django.views.generic import ListView
# from rest_framework.views import APIView



class QuizesList(ListView):
    model = Quiz
    template_name = 'templates/quizes.html'
 

def quize_detail(request, pk):
    context = {
        'quize': Quiz.objects.get(pk=pk)
    }
    return render(request, 'templates/quize_details.html', context)        
