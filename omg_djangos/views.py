from django.shortcuts import render

def index(request):
    """Página principal do omg_djangos"""



    return render(request, 'omg_djangos/index.html')
# Create your views here.
