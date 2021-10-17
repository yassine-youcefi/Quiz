from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.views.generic import ListView



def index(request):
    
    return render(request, 'templates/index.html')


