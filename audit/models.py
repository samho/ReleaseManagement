from django.db import models


# Create your models here.
class OperationAudit(models.Model):
    user_id = models.IntegerField(default=0)
    operation_id = models.IntegerField(default=0)
    created_at = models.DateTimeField('Date of the audit log created.')


class Operation(models.Model):
    operation_shot = models.CharField(max_length=100)
    operation_detail = models.CharField(max_length=500)