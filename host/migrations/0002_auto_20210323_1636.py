# Generated by Django 2.2.19 on 2021-03-23 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='hostappmapping',
            name='app_id',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='hostappmapping',
            name='app_status',
            field=models.CharField(db_index=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='hostappmapping',
            name='host_id',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='hostbaseconfig',
            name='host_id',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='hostlogininfo',
            name='host_id',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='hostnetwork',
            name='host_id',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='hostservicemapping',
            name='host_id',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='hostservicemapping',
            name='service_id',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='hostservicemapping',
            name='service_status',
            field=models.CharField(db_index=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='hoststorage',
            name='host_id',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
