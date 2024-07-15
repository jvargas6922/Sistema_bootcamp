from django.shortcuts import render
from django.http import HttpResponse
from .models import Module

# Create your views here.
def index(request):
    # listado de modulos
    modules = Module.objects.select_related('id_bootcamp').all()
    context ={'modules': modules}
    return render(request, 'module/index.html', context)
