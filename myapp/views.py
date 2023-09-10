from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import models

from . import forms


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
        render(request, 'projects/projects.html', {'proyectos': proyectos})
    )


def tasks(request):

    lista_tareas = models.Task.objects.all()

    titulo = 'Tareas'
    return render(request, 'tasks/tasks.html', {'tareas': titulo, 'tasks': lista_tareas})


# defino la vista para formularios
# si quiero agregar al modelo Task
# tener en cuenta que una tarea pertenece a un proyecto, puesto que el id de proyecto es foreign key
def task_form(request):
    if request.method == 'GET':
        return render(request, 'tasks/task_form.html', 
            {'formulario': forms.Create_new_task()}
        )     
    else: # si es por else probablemente es un POST

        task_title = request.POST['title']
        task_description = request.POST['description']
 
        # llamo a la base de datos para crear una nueva instancia
        models.Task.objects.create(title=task_title, description=task_description, project_id=2)
        
        return redirect('tareas_lista')


def projects_form(request):
        
        if request.method == 'GET':
        
            return render(request, 'projects/projects_form.html', {
                'nuevo_proyecto': forms.Create_new_project()
            })
        else:
            print(request.POST)

            models.Project.objects.create(
                name= request.POST['name']
            )
            
            return redirect('proyectos_lista')
    
