from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # url
    path('topics', views.topics, name='topics'), # url/topics
]
