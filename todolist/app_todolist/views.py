from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from .models import Tarefa
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def segunda(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()

        if titulo:
            Tarefa.objects.create(titulo=titulo, dia_semana="SEG")
            return redirect("segunda")
        
    tarefas = Tarefa.objects.filter(dia_semana="SEG").order_by("-id")
    return render (request, "segunda.html", {"tarefas":tarefas})

@require_POST
def deletar_tarefa(request,id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect("segunda")

@require_http_methods(["GET", "POST"])
def editar_tarefa(request,id):
    tarefa = get_object_or_404(Tarefa, id=id)

    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        if titulo:
            tarefa.titulo = titulo
            tarefa.save()
            return redirect("segunda")
        
    return render(request, "editar_tarefa.html", {"tarefa": tarefa})