# Generated by Django 3.0.6 on 2020-05-12 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20200512_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='showcase',
        ),
    ]
