# Generated by Django 3.0.6 on 2020-06-06 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_auto_20200605_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
