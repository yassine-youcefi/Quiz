from django.urls import path, include

from .views import UserView, QuestionsListView, QuizListView

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('user/', UserView.as_view(), name='user'),
    path('questions/', QuestionsListView.as_view(), name='questions'),
    path('quizzes/', QuizListView.as_view(), name='quiz'),
]