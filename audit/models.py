from django.db import models


# Create your models here.
class OperationAudit(models.Model):
    user_id = models.IntegerField(default=0, db_index=True)
    operation_id = models.IntegerField(default=0, db_index=True)
    created_at = models.DateTimeField('Date of the audit log created.', db_index=True)

    def __str__(self):
        return "User: %d -> Operation: %d" % (self.user_id, self.operation_id)


class Operation(models.Model):
    operation_shot = models.CharField(max_length=100)
    operation_detail = models.CharField(max_length=500)

    def __str__(self):
        return self.operation_shot
