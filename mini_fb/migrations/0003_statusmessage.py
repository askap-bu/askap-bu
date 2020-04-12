# Generated by Django 2.2.7 on 2020-04-01 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0002_auto_20200328_0314'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(blank=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mini_fb.Profile')),
            ],
        ),
    ]