from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    comment = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField('Date of creating project.')

    def __str__(self):
        return self.name


class ProjectUserMapping(models.Model):
    project_id = models.IntegerField(default=0, db_index=True)
    user_id = models.IntegerField(default=0, db_index=True)

    def __str__(self):
        return "Project: %d -> User: %d" % (self.project_id, self.user_id)


class ProjectAppMapping(models.Model):
    project_id = models.IntegerField(default=0, db_index=True)
    app_id = models.IntegerField(default=0, db_index=True)

    def __str__(self):
        return "Project: %d -> Application: %d" % (self.project_id, self.app_id)


