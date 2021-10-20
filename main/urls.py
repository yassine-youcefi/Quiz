from django.urls import path
from .views import (
    QuizzesList,
    quiz_detail,
    quiz_data,
    quiz_result,
    index
)

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('quiz/',QuizzesList.as_view() , name='quiz_list'),
    path('quiz/<int:pk>/', quiz_detail, name='quiz_detail'),
    path('quiz/<int:pk>/data/', quiz_data, name='quiz_data'),
    path('quiz/<int:pk>/results/', quiz_result, name='quiz_results'),
]

