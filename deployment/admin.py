from django.contrib import admin

# Register your models here.
from .models import Task, TaskAnsible, TaskRunResult, TaskAppMapping, TaskHostMapping, TaskServiceMapping

admin.site.register(Task)
admin.site.register(TaskAnsible)
admin.site.register(TaskRunResult)
admin.site.register(TaskAppMapping)
admin.site.register(TaskHostMapping)
admin.site.register(TaskServiceMapping)
