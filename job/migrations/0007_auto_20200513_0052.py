# Generated by Django 3.0.6 on 2020-05-12 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_remove_job_showcase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='role',
            field=models.CharField(max_length=100),
        ),
    ]