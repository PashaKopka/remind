# Generated by Django 3.2.4 on 2021-07-04 16:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210621_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 4, 16, 4, 20, 703990, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='list',
            name='date_of_creation',
            field=models.DateField(default=datetime.datetime(2021, 7, 4, 16, 4, 20, 705985, tzinfo=utc), verbose_name='date_of_creation_remind'),
        ),
        migrations.AlterField(
            model_name='note',
            name='date_of_creation',
            field=models.DateField(default=datetime.datetime(2021, 7, 4, 16, 4, 20, 705985, tzinfo=utc), verbose_name='date_of_creation_remind'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_of_creation',
            field=models.DateField(default=datetime.datetime(2021, 7, 4, 16, 4, 20, 705985, tzinfo=utc), verbose_name='date_of_creation_remind'),
        ),
    ]
