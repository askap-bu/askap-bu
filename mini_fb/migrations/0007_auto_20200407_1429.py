# Generated by Django 2.2.7 on 2020-04-07 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0006_statusmessage_status_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statusmessage',
            old_name='status_image',
            new_name='image',
        ),
    ]
