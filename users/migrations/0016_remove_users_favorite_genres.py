# Generated by Django 3.0.6 on 2021-03-15 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20210316_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='favorite_genres',
        ),
    ]
