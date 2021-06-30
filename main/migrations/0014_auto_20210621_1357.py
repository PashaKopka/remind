# Generated by Django 3.2.4 on 2021-06-21 10:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210621_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='filename',
            field=models.CharField(default='file', max_length=150),
        ),
        migrations.AlterField(
            model_name='file',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 21, 10, 57, 1, 798239, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='list',
            name='date_of_creation',
            field=models.DateField(default=datetime.datetime(2021, 6, 21, 10, 57, 1, 800233, tzinfo=utc), verbose_name='date_of_creation_remind'),
        ),
        migrations.AlterField(
            model_name='note',
            name='date_of_creation',
            field=models.DateField(default=datetime.datetime(2021, 6, 21, 10, 57, 1, 800233, tzinfo=utc), verbose_name='date_of_creation_remind'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_of_creation',
            field=models.DateField(default=datetime.datetime(2021, 6, 21, 10, 57, 1, 800233, tzinfo=utc), verbose_name='date_of_creation_remind'),
        ),
    ]