from django.db import models

# Create your models here.


class Feature(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    comment = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name


class TestPlan(models.Model):
    app_id = models.IntegerField(db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    comment = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name


class CheckPoint(models.Model):
    feature_id = models.IntegerField(db_index=True)
    title = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class FeatureCheckPointMapping(models.Model):
    feature_id = models.IntegerField(db_index=True)
    checkpoint_id = models.IntegerField(db_index=True)

    def __str__(self):
        return "Feature: %d -> Check Point: %d" % (self.feature_id, self.checkpoint_id)


class TestCase(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    check_point_id = models.IntegerField()
    steps = models.CharField(max_length=500)
    excepted_result = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class TestTask(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, db_index=True)
    progress = models.FloatField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name


class TestCaseTaskRun(models.Model):
    task_id = models.IntegerField(db_index=True)
    case_id = models.IntegerField(db_index=True)
    status = models.CharField(max_length=20, default="None")
    run_date = models.DateTimeField()

    def __str__(self):
        return "Test Task: %d -> Test Case: %d" % (self.task_id, self.case_id)
