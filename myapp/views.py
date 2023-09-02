from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models

from .forms import Create_new_task


def index(request):
    titulo = 'Pagina Principan en Django'

    return render(
        request,
        'index.html',
        {'title': titulo}
    )


def about(request):
    return render(request, 'about.html')


def projects(request):

    # consulta de la tabla Project, pido que me traiga todos los objetos
    proyectos = models.Project.objects.all()

    # Retorno... renderiza el archivo html con la consulta como parametro
    return (
        render(request, 'projects.html', {'proyectos': proyectos})
    )


def tasks(request):

    lista_tareas = models.Task.objects.all()

    titulo = 'Tareas'
    return render(request, 'tasks.html', {'tareas': titulo, 'tasks': lista_tareas})


# defino la vista para formularios
def task_form(request):
    return render(request, 'task_form.html', {
        'formulario': Create_new_task()
    }
    )
