# Generated by Django 2.2.7 on 2020-03-31 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20200331_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='person',
            field=models.ForeignKey(default=1, on_delete='CASCADE', to='quotes.Person'),
            preserve_default=False,
        ),
    ]
