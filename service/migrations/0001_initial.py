# Generated by Django 2.2.19 on 2021-03-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServicePort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.IntegerField(default=0)),
                ('service_port', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
