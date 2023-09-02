from django.contrib import admin

# Register your models here.
from . import models


# para que se pueda visualizar las tablas en admin
admin.site.register(models.Project)
admin.site.register(models.Task)