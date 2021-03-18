from django.contrib import admin

# Register your models here.
from .models import User, Role, UserRoleMapping

admin.site.register(User)
admin.site.register(Role)
admin.site.register(UserRoleMapping)
