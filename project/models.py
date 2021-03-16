from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField('Date of creating project.')


class ProjectUserMapping(models.Model):
    project_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)


class ProjectAppMapping(models.Model):
    project_id = models.IntegerField(default=0)
    app_id = models.IntegerField(default=0)


