from django.shortcuts import render
from .models import Topic

def index(request):
    """Página principal do omg_djangos"""
    return render(request, 'omg_djangos/index.html')

def topics(request):
    """Motra todos os assuntos"""
    topics = Topic.objects.order_by("date_added")
    context = {"topics":topics}
    return render(request, 'omg_djangos/topics.html', context)

def topic(request, topic_id):
    """Motra um unico assunto pelo id todas as sua entradas"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {"topic": topic, 'entries': entries}
    return render(request, 'omg_djangos/topic.html', context)
