# Generated by Django 3.1 on 2020-09-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0003_auto_20200927_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='every_day_remind',
            field=models.TimeField(default=None, null=True, verbose_name='EveryDayRemind'),
        ),
    ]
