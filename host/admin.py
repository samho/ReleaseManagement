from django.contrib import admin

# Register your models here.
from .models import Host, HostBaseConfig, HostStorage, HostNetwork, HostLoginInfo, HostAppMapping, HostServiceMapping

admin.site.register(Host)
admin.site.register(HostBaseConfig)
admin.site.register(HostStorage)
admin.site.register(HostNetwork)
admin.site.register(HostLoginInfo)
admin.site.register(HostAppMapping)
admin.site.register(HostServiceMapping)
