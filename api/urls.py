from django.urls import path, include

from .views import (UserView,
                    QuestionsListView, 
                    QuizListView,QuizView,
                    QuestionsListQuizView,
                    QuestionCreateView, 
                    QuestionView)

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('user/', UserView.as_view(), name='user'),
    path('questions/', QuestionsListView.as_view(), name='questions'),
    path('question/<int:pk>/', QuestionView.as_view(), name='question'),
    path('question/', QuestionCreateView.as_view(), name='question-create'),


    path('quizzes/', QuizListView.as_view(), name='quizzes'),
    # path('quiz/', PostQuizView.as_view(), name='quiz-post'),
    path('quiz/<int:pk>/questions/', QuestionsListQuizView.as_view(), name='questions-quiz'),
    path('quiz/<int:pk>/', QuizView.as_view(), name='quiz'),

]