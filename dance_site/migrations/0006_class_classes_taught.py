# Generated by Django 2.2.7 on 2020-04-14 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dance_site', '0005_auto_20200414_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='classes_taught',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dance_site.Teacher'),
        ),
    ]
