# Generated by Django 2.2.7 on 2020-03-28 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='email',
            new_name='email_address',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='profile_image',
            new_name='profile_image_url',
        ),
    ]
