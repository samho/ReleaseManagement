# Generated by Django 2.2.19 on 2021-04-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20210323_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField(db_index=True)),
                ('feature_id', models.IntegerField(db_index=True)),
                ('comment', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='version',
            field=models.CharField(default='None', max_length=20),
        ),
    ]