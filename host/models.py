from django.db import models


# Create your models here.
class Host(models.Model):
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField('Date of host created.')


class HostBaseConfig(models.Model):
    host_id = models.IntegerField(default=0)
    cpu_core = models.IntegerField(default=0)
    memory = models.IntegerField(default=0)


class HostStorage(models.Model):
    host_id = models.IntegerField(default=0)
    storage_type = models.CharField(max_length=50)
    storage_size = models.IntegerField()


class HostNetwork(models.Model):
    host_id = models.IntegerField(default=0)
    network_type = models.CharField(max_length=10)
    network_value = models.CharField(max_length=50)


class HostLoginInfo(models.Model):
    host_id = models.IntegerField(default=0)
    login_method = models.CharField(max_length=100)
    login_port = models.IntegerField()
    login_user = models.CharField(max_length=100)
    login_password = models.CharField(max_length=100, null=True)
    login_key = models.CharField(max_length=500, null=True)


class HostAppMapping(models.Model):
    host_id = models.IntegerField(default=0)
    app_id = models.IntegerField(default=0)
    app_status = models.CharField(max_length=20)


class HostServiceMapping(models.Model):
    host_id = models.IntegerField(default=0)
    service_id = models.IntegerField(default=0)
    service_status = models.CharField(max_length=20)



