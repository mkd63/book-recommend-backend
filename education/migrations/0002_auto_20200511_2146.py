# Generated by Django 2.2.2 on 2020-05-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]