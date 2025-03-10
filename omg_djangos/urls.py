#aqui são as rotas
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # url
    path('topics', views.topics, name='topics'), # url/topics
    path('topics/<topic_id>/', views.topic, name='topic'), # url/topics/n
    path('new_topic', views.new_topic, name='new_topic'), # url/new_topic
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'), # url/new_entry/n
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry')
]
