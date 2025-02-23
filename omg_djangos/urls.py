#aqui são as rotas
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # url
    path('topics', views.topics, name='topics'), # url/topics
    path('topic/<topic_id>/', views.topic, name='topic'), # url/topics
]
