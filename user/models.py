from django.db import models


# Create your models here.
class User(models.Model):
    real_name = models.CharField(max_length=50, db_index=True)
    user_name = models.CharField(max_length=100, db_index=True)
    email = models.CharField(max_length=200, db_index=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField('Date for created.')
    updated_at = models.DateTimeField('Date of updated.')

    def __str__(self):
        return self.real_name


class Role(models.Model):
    role_name = models.CharField(max_length=50, db_index=True)
    comment = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.role_name


class UserRoleMapping(models.Model):
    user_id = models.IntegerField(db_index=True)
    role_id = models.IntegerField(db_index=True)

    def __str__(self):
        return "User: %d -> Role: %d" % (self.user_id, self.role_id)

