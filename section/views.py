from django.shortcuts import render
from django.http import HttpResponse
from .models import Section
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    #listado de Secciones
    sections = Section.objects.select_related('id_module').all()
    context ={'sections':sections}
    return render(request, 'section/index.html',context)
