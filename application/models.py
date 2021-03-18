from django.db import models


# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=300, null=True)
    created_at = models.DateTimeField

    def __str__(self):
        return self.name


class ApplicationPort(models.Model):
    app_id = models.IntegerField()
    port = models.IntegerField()
    comment = models.CharField(max_length=100)

    def __str__(self):
        return "Application: %d -> Port: %d" % (self.app_id, self.port)


