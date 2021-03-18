from django.contrib import admin

# Register your models here.
from .models import OperationAudit, Operation

admin.site.register(OperationAudit)
admin.site.register(Operation)
