from django.contrib import admin

# Register your models here.
from .models import Project, ProjectUserMapping, ProjectAppMapping

admin.site.register(Project)
admin.site.register(ProjectUserMapping)
admin.site.register(ProjectAppMapping)
