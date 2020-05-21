# Generated by Django 3.0.6 on 2020-05-21 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200516_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='key_expires',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='verification_key',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]