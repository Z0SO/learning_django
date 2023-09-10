
from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='root'),
    path('sobre-nosotros/', views.about, name='about'),
    path('proyectos/', views.projects, name='proyectos_lista'),
    path('tareas/', views.tasks, name='tareas_lista'),
    path('tareas_formulario/', views.task_form, name='tareas_new'),
    path('projects_formulario/', views.projects_form, name='proyectos_new'), 
]