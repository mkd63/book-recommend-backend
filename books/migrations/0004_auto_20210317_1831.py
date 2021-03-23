# Generated by Django 3.0.6 on 2021-03-17 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_books_cropped_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['-rating']},
        ),
        migrations.AddField(
            model_name='books',
            name='google_link',
            field=models.CharField(default='http://www.google.co.in', max_length=200),
            preserve_default=False,
        ),
    ]