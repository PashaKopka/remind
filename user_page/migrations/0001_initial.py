# Generated by Django 3.1 on 2020-08-30 19:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('list', models.TextField(verbose_name='List')),
                ('style', models.CharField(default=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_page.user', verbose_name='User'), max_length=300, verbose_name='Style')),
                ('remind', models.DateTimeField(default=0, null=True, verbose_name='Remind')),
                ('deadline', models.DateTimeField(default=0, null=True, verbose_name='Remind')),
                ('done', models.BooleanField(default=False, verbose_name='Done')),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
                ('date_of_adding', models.DateTimeField(default=0, null=True, verbose_name='Remind')),
            ],
            options={
                'verbose_name': 'List',
                'verbose_name_plural': 'Lists',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('files', models.FileField(upload_to='user_files/', verbose_name='File')),
                ('style', models.CharField(default=False, max_length=300, verbose_name='Style')),
                ('remind', models.DateTimeField(default=0, null=True, verbose_name='Remind')),
                ('deadline', models.DateTimeField(default=0, null=True, verbose_name='Remind')),
                ('done', models.BooleanField(default=False, verbose_name='Done')),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
                ('date_of_adding', models.DateTimeField(default=datetime.datetime.now, verbose_name='Remind')),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=100, verbose_name='Login')),
                ('email', models.CharField(max_length=100, verbose_name='Login')),
                ('password', models.CharField(max_length=80, verbose_name='Password')),
                ('theme', models.CharField(max_length=100, verbose_name='Theme')),
                ('default_style_note', models.CharField(max_length=300, verbose_name='Style')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('style', models.CharField(max_length=300, verbose_name='Style')),
                ('every_day_remind', models.TimeField(default=0, null=True, verbose_name='EveryDayRemind')),
                ('deadline', models.DateTimeField(default=0, null=True, verbose_name='Remind')),
                ('done', models.BooleanField(default=False, verbose_name='Done')),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
                ('date_of_adding', models.DateTimeField(default=0, null=True, verbose_name='Remind')),
                ('list_id', models.ManyToManyField(to='user_page.List', verbose_name='List')),
                ('note_id', models.ManyToManyField(to='user_page.Note', verbose_name='Note')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_page.user', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_page.user', verbose_name='User'),
        ),
        migrations.AddField(
            model_name='list',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_page.user', verbose_name='User'),
        ),
    ]
