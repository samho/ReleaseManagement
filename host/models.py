from django.db import models


# Create your models here.
class Host(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    comment = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField('Date of host created.')

    def __str__(self):
        return self.name


class HostBaseConfig(models.Model):
    host_id = models.IntegerField(default=0, db_index=True)
    cpu_core = models.IntegerField(default=0)
    memory = models.IntegerField(default=0)

    def __str__(self):
        return self.host_id


class HostStorage(models.Model):
    host_id = models.IntegerField(default=0, db_index=True)
    storage_type = models.CharField(max_length=50)
    storage_size = models.IntegerField()

    def __str__(self):
        return "Host: %d -> Type: %s" % (self.host_id, self.storage_type)


class HostNetwork(models.Model):
    host_id = models.IntegerField(default=0, db_index=True)
    network_type = models.CharField(max_length=10)
    network_value = models.CharField(max_length=50)

    def __str__(self):
        return "Host: %d -> Type: %s" % (self.host_id, self.network_type)


class HostLoginInfo(models.Model):
    host_id = models.IntegerField(default=0, db_index=True)
    login_method = models.CharField(max_length=100)
    login_port = models.IntegerField()
    login_user = models.CharField(max_length=100)
    login_password = models.CharField(max_length=100, null=True)
    login_key = models.CharField(max_length=500, null=True)

    def __str__(self):
        return "Host: %d -> Type: %s" % (self.host_id, self.login_method)


class HostAppMapping(models.Model):
    host_id = models.IntegerField(default=0, db_index=True)
    app_id = models.IntegerField(default=0, db_index=True)
    app_status = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return "Host: %d -> Application: %d" % (self.host_id, self.app_id)


class HostServiceMapping(models.Model):
    host_id = models.IntegerField(default=0, db_index=True)
    service_id = models.IntegerField(default=0, db_index=True)
    service_status = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return "Host: %d -> Service: %d" % (self.host_id, self.service_id)



