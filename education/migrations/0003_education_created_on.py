# Generated by Django 3.0.6 on 2020-05-23 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20200511_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
