# Generated by Django 3.0.6 on 2021-03-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210317_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='about_text',
            field=models.CharField(max_length=3000),
        ),
    ]
