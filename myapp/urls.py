
from django.urls import path
from . import views


urlpatterns=[
    path('', views.index),
    path('about/', views.about),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('task_form/', views.task_form),
]