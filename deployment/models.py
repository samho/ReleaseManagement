from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200, null=True)
    task_method = models.CharField(max_length=50)
    created_at = models.DateTimeField('Date of task created.')

    def __str__(self):
        return self.name


class TaskAnsible(models.Model):
    task_id = models.IntegerField(default=0)
    playbook_path = models.CharField(max_length=100, default='/etc/ansible/')
    playbook_name = models.CharField(max_length=100, default='default.yml')

    def __str__(self):
        return self.task_id


class TaskHostMapping(models.Model):
    host_id = models.IntegerField(default=0)
    task_id = models.IntegerField(default=0)

    def __str__(self):
        return "Task: %d -> Host: %d" % (self.task_id, self.host_id)


class TaskAppMapping(models.Model):
    app_id = models.IntegerField(default=0)
    task_id = models.IntegerField(default=0)

    def __str__(self):
        return "Task: %d -> Application: %d" % (self.task_id, self.app_id)


class TaskRunResult(models.Model):
    task_id = models.IntegerField(default=0)
    status = models.CharField(max_length=100)
    result_content = models.TextField()
    started_at = models.DateTimeField("Datetime of the task startup.")
    end_at = models.DateTimeField("Datetime of the task stop.")

    def __str__(self):
        return self.task_id


class TaskServiceMapping(models.Model):
    task_id = models.IntegerField(default=0)
    service_id = models.IntegerField(default=0)

    def __str__(self):
        return "Task: %d -> Service: %d" % (self.task_id, self.service_id)



