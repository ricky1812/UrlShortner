# Generated by Django 2.0.5 on 2019-01-20 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0003_remove_bitly_keys'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitly',
            name='keys',
            field=models.CharField(default='shortn', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
