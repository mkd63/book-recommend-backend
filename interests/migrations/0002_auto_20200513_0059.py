# Generated by Django 3.0.6 on 2020-05-12 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interests',
            old_name='interest_name',
            new_name='name',
        ),
    ]
