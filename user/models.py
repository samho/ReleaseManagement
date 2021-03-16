from django.db import models


# Create your models here.
class User(models.Model):
    real_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField('Date for created.')
    updated_at = models.DateTimeField('Date of updated.')


class Role(models.Model):
    role_name = models.CharField(max_length=50)
    comment = models.CharField(max_length=100, null=True)


class UserRoleMapping(models.Model):
    user_id = models.IntegerField()
    role_id = models.IntegerField()

