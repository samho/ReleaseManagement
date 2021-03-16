from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200, null=True)
    task_method = models.CharField(max_length=50)
    created_at = models.DateTimeField('Date of task created.')


class TaskAnsible(models.Model):
    task_id = models.IntegerField(default=0)
    playbook_path = models.CharField(max_length=100, default='/etc/ansible/')
    playbook_name = models.CharField(max_length=100, default='default.yml')


class TaskHostMapping(models.Model):
    host_id = models.IntegerField(default=0)
    task_id = models.IntegerField(default=0)


class TaskAppMapping(models.Model):
    app_id = models.IntegerField(default=0)
    task_id = models.IntegerField(default=0)


class TaskRunResult(models.Model):
    task_id = models.IntegerField(default=0)
    status = models.CharField(max_length=100)
    result_content = models.TextField()
    started_at = models.DateTimeField("Datetime of the task startup.")
    end_at = models.DateTimeField("Datetime of the task stop.")


class TaskServiceMapping(models.Model):
    task_id = models.IntegerField(default=0)
    service_id = models.IntegerField(default=0)




