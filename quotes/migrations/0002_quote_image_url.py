# Generated by Django 2.2.7 on 2020-03-25 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
