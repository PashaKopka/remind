# Generated by Django 3.1 on 2020-09-27 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0002_auto_20200927_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='every_day_remind',
            field=models.TimeField(default=django.db.models.deletion.SET_NULL, null=True, verbose_name='EveryDayRemind'),
        ),
    ]
