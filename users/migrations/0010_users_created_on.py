# Generated by Django 3.0.6 on 2020-05-21 01:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200521_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
