# Generated by Django 2.2.19 on 2021-03-23 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='serviceport',
            name='service_id',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='serviceport',
            name='service_port',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]