from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Teste")

def segunda(request):
    tarefas = Tarefa.objects.filter(dia_semana="SEG")
    return render (request, "segunda.html", {"tarefas":tarefas})