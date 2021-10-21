from django.urls import path
from .views import (
    QuizzesList,
    quiz_detail,
    quiz_data,
    quiz_result,
    quiz_create,
    quiz_update, 
    index
)

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('quiz/',QuizzesList.as_view() , name='quiz_list'),
    path('quiz/<int:pk>/', quiz_detail, name='quiz_detail'),
    path('quiz/<int:pk>/data/', quiz_data, name='quiz_data'),
    path('quiz/<int:pk>/results/', quiz_result, name='quiz_results'),
    path('quiz/create/', quiz_create, name='quiz_create'),
    path('quiz/<int:pk>/update/', quiz_update, name='quiz_update'),
    
]

