# Generated by Django 4.1.7 on 2023-03-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='experiance',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
    ]