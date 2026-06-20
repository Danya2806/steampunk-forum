from django.urls import path
from . import views

urlpatterns = [
    path('', views.topic_list, name='topic_list'),
    path('topic/<int:pk>/', views.topic_detail, name='topic_detail'),
    path('topics/new/', views.create_topic, name='create_topic'),
    path('register/', views.register, name='register'), # <-- Новый маршрут
]