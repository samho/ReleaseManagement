# Generated by Django 2.2.19 on 2021-03-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(verbose_name='Date of creating project.')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAppMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField(default=0)),
                ('app_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUserMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
            ],
        ),
    ]
