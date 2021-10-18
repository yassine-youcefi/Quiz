from django.urls import path
from .views import (
    QuizesList,
    quize_detail
)

app_name = 'main'

urlpatterns = [
    path('',QuizesList.as_view() , name='quize_list'),
    path('<int:pk>/', quize_detail, name='quize_detail'),
]

