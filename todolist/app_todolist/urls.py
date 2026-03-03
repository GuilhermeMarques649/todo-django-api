from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("segunda/", views.segunda, name="segunda"),
    path("tarefa/<int:id>/deletar/", views.deletar_tarefa, name="deletar_tarefa"),
    path("tarefa/<int:id>/editar/", views.editar_tarefa, name="editar_tarefa")
]