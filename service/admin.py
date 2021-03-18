from django.contrib import admin

# Register your models here.
from .models import Service, ServicePort

admin.site.register(Service)
admin.site.register(ServicePort)
