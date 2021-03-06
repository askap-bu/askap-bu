# Generated by Django 2.2.7 on 2020-04-13 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True)),
                ('last_name', models.TextField(blank=True)),
                ('city', models.TextField(blank=True)),
                ('email_address', models.TextField(blank=True)),
                ('profile_image_url', models.URLField(blank=True)),
                ('birth_date', models.DateField(blank=True)),
                ('classes', models.ManyToManyField(related_name='_teacher_classes_+', to='dance_site.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True)),
                ('last_name', models.TextField(blank=True)),
                ('city', models.TextField(blank=True)),
                ('email_address', models.TextField(blank=True)),
                ('profile_image_url', models.URLField(blank=True)),
                ('birth_date', models.DateField(blank=True)),
                ('classes', models.ManyToManyField(related_name='_student_classes_+', to='dance_site.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.TextField(blank=True)),
                ('class_name', models.TextField(blank=True)),
                ('class_picture', models.URLField(blank=True)),
                ('price', models.TextField(blank=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dance_site.Teacher')),
            ],
        ),
    ]
