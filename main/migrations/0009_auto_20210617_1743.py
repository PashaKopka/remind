# Generated by Django 3.2.4 on 2021-06-17 14:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210617_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 17, 14, 43, 12, 62163, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='list',
            name='date_of_creation',
            field=models.DateField(default=datetime.datetime(2021, 6, 17, 14, 43, 12, 65147, tzinfo=utc), verbose_name='date_of_creation_remind'),
        ),
        migrations.AlterField(
            model_name='note',
            name='date_of_creation',
            field=models.DateField(default=datetime.datetime(2021, 6, 17, 14, 43, 12, 65147, tzinfo=utc), verbose_name='date_of_creation_remind'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_of_creation',
            field=models.DateField(default=datetime.datetime(2021, 6, 17, 14, 43, 12, 65147, tzinfo=utc), verbose_name='date_of_creation_remind'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lists',
            field=models.ManyToManyField(blank=True, related_name='user_lists', to='main.List'),
        ),
        migrations.AlterField(
            model_name='user',
            name='notes',
            field=models.ManyToManyField(blank=True, related_name='user_notes', to='main.Note'),
        ),
        migrations.AlterField(
            model_name='user',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='user_projects', to='main.Project'),
        ),
    ]
