from django.contrib import admin

# Register your models here.
from .models import Application, ApplicationPort

admin.site.register(Application)
admin.site.register(ApplicationPort)
