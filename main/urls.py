from django.urls import path
from .views import (
    QuizzesList,
    QuizzesListAdmin,
    quiz_detail,
    quiz_data,
    quiz_result,
    quiz_create,
    quiz_update, 
    quize_delete,
    question_create,
    quiz_detail_admin,
    index
)

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('quiz/',QuizzesList.as_view() , name='quiz_list'),
    path('quiz/admin/',QuizzesListAdmin.as_view() , name='quiz_list_admin'),

    path('quiz/<int:pk>/', quiz_detail, name='quiz_detail'),
    path('quiz/<int:pk>/data/', quiz_data, name='quiz_data'),
    path('quiz/<int:pk>/results/', quiz_result, name='quiz_results'),
    path('quiz/create/', quiz_create, name='quiz_create'),
    path('quiz/admin/<int:pk>/update/', quiz_update, name='quiz_update'),
    path('quiz/admin/<int:pk>/delete/', quize_delete, name='quiz_delete'),
    path('quiz/admin/<int:pk>/update/question/create/', question_create, name='question_create'),
    path('quiz/<int:pk>/admin/', quiz_detail_admin, name='quiz_detail_admin'),
]

