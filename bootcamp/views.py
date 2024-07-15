from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .models import Bootcamp
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    # DATA BOOTCAMP = SELECT * FROM BOOTCAMP
    bootcamps = Bootcamp.objects.all()
    context = {'bootcamps': bootcamps }
    return render(request, 'bootcamp/index.html',context)

@login_required
def create(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        bootcamp_name = data.get('bootcamp')
    except (json.JSONDecodeError, TypeError):
        bootcamp_name = request.POST.get('bootcamp')
    if bootcamp_name:
        bootcamp = Bootcamp(bootcamp=bootcamp_name)
        bootcamp.save()
        return JsonResponse({'message': 'Bootcamp creado exitosamente'},status=201)
    else:
        return JsonResponse({'error': 'El nombre del bootcamp no fue proporcionado.'}, status=400)







