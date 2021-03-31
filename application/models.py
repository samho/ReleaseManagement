from django.db import models


# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    comment = models.CharField(max_length=300, null=True)
    version = models.CharField(max_length=20)
    created_at = models.DateTimeField

    def __str__(self):
        return self.name


class ApplicationPort(models.Model):
    app_id = models.IntegerField(db_index=True)
    port = models.IntegerField(db_index=True)
    comment = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "Application: %d -> Port: %d" % (self.app_id, self.port)


class ApplicationFeatures(models.Model):
    app_id = models.IntegerField(db_index=True)
    feature_id = models.IntegerField(db_index=True)
    comment = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "Application: %d -> feature: %d" % (self.app_id, self.feature_id)
