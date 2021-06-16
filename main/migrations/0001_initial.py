# Generated by Django 3.2.4 on 2021-06-16 14:32

import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/%Y/%m/%d')),
                ('datetime', models.DateTimeField(default=datetime.datetime(2021, 6, 16, 14, 32, 9, 229742, tzinfo=utc))),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateField(default=datetime.datetime(2021, 6, 16, 14, 32, 9, 232736, tzinfo=utc), verbose_name='date_of_creation_remind')),
                ('date_of_change', models.DateField(blank=True, verbose_name='date_of_changing_remind')),
                ('draft', models.BooleanField()),
                ('title', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'List',
                'verbose_name_plural': 'Lists',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateField(default=datetime.datetime(2021, 6, 16, 14, 32, 9, 232736, tzinfo=utc), verbose_name='date_of_creation_remind')),
                ('date_of_change', models.DateField(blank=True, verbose_name='date_of_changing_remind')),
                ('draft', models.BooleanField()),
                ('title', models.CharField(blank=True, max_length=50)),
                ('text', models.TextField()),
                ('files', models.ManyToManyField(blank=True, to='main.File')),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(blank=True, max_length=50)),
                ('date', models.DateField(blank=True, verbose_name='date_of_notification')),
                ('time', models.TimeField(verbose_name='time_of_notification')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateField(default=datetime.datetime(2021, 6, 16, 14, 32, 9, 232736, tzinfo=utc), verbose_name='date_of_creation_remind')),
                ('date_of_change', models.DateField(blank=True, verbose_name='date_of_changing_remind')),
                ('draft', models.BooleanField()),
                ('title', models.CharField(max_length=50)),
                ('deadline', models.ManyToManyField(related_name='deadline', to='main.Notification')),
                ('lists', models.ManyToManyField(to='main.List')),
                ('notes', models.ManyToManyField(to='main.Note')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Settings',
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.CharField(max_length=50)),
                ('font_color', models.CharField(max_length=50)),
                ('font_size', models.IntegerField()),
                ('font_width', models.IntegerField()),
                ('border_radius', models.IntegerField()),
                ('border_color', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Style',
                'verbose_name_plural': 'Styles',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('lists', models.ManyToManyField(related_name='user_lists', to='main.List')),
                ('notes', models.ManyToManyField(related_name='user_notes', to='main.Note')),
                ('projects', models.ManyToManyField(related_name='user_projects', to='main.Project')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_settings', to='main.settings')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='settings',
            name='default_theme',
            field=models.ManyToManyField(to='main.Style'),
        ),
        migrations.AddField(
            model_name='project',
            name='style',
            field=models.ManyToManyField(to='main.Style'),
        ),
        migrations.AddField(
            model_name='project',
            name='time_of_notification',
            field=models.ManyToManyField(blank=True, related_name='time_of_notification', to='main.Notification'),
        ),
        migrations.AddField(
            model_name='note',
            name='style',
            field=models.ManyToManyField(to='main.Style'),
        ),
        migrations.CreateModel(
            name='ListElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('done', models.BooleanField(default=False)),
                ('file', models.ManyToManyField(blank=True, to='main.File')),
            ],
            options={
                'verbose_name': 'List element',
                'verbose_name_plural': 'List elements',
            },
        ),
        migrations.AddField(
            model_name='list',
            name='list_elements',
            field=models.ManyToManyField(related_name='elements_of_this_list', to='main.ListElement'),
        ),
        migrations.AddField(
            model_name='list',
            name='notification',
            field=models.ManyToManyField(related_name='notification', to='main.Notification'),
        ),
        migrations.AddField(
            model_name='list',
            name='style',
            field=models.ManyToManyField(to='main.Style'),
        ),
    ]
