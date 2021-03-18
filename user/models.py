from django.db import models


# Create your models here.
class User(models.Model):
    real_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField('Date for created.')
    updated_at = models.DateTimeField('Date of updated.')

    def __str__(self):
        return self.real_name


class Role(models.Model):
    role_name = models.CharField(max_length=50)
    comment = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.role_name


class UserRoleMapping(models.Model):
    user_id = models.IntegerField()
    role_id = models.IntegerField()

    def __str__(self):
        return "User: %d -> Role: %d" % (self.user_id, self.role_id)

