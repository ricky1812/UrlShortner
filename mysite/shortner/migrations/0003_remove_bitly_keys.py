# Generated by Django 2.0.5 on 2019-01-20 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0002_auto_20190120_0653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bitly',
            name='keys',
        ),
    ]