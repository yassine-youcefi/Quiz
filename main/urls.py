from django.urls import path
from .views import (
    QuizzesList,
    quiz_detail,
    index
)

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('quiz/',QuizzesList.as_view() , name='quiz_list'),
    path('quiz/<int:pk>/', quiz_detail, name='quiz_detail'),

]

