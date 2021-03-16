from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=100, null=True)


class ServicePort(models.Model):
    service_id = models.IntegerField(default=0)
    service_port = models.IntegerField(default=0)
    comment = models.CharField(max_length=100, null=True)
