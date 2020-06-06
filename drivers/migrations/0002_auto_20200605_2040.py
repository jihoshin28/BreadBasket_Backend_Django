# Generated by Django 3.0.6 on 2020-06-06 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='email',
            field=models.EmailField(default='email', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='phone',
            field=models.IntegerField(default=-5555),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='state',
            field=models.CharField(default='state', max_length=20),
            preserve_default=False,
        ),
    ]