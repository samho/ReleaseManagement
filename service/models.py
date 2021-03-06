from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    comment = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class ServicePort(models.Model):
    service_id = models.IntegerField(default=0, db_index=True)
    service_port = models.IntegerField(default=0, db_index=True)
    comment = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "Service: %d -> Port: %d" % (self.service_id, self.service_port)
