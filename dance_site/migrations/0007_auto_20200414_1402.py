# Generated by Django 2.2.7 on 2020-04-14 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dance_site', '0006_class_classes_taught'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='classes_taught',
            new_name='teaches_taught',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='classes_taught',
            new_name='teaches_taught',
        ),
    ]
