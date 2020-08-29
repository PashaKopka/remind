from django.contrib.auth.models import User as StandartUser
from django.db import models


class User(StandartUser):
    """User Model"""
    id = models.AutoField(primary_key=True)
    login = models.CharField('Login', max_length=100)
    password = models.CharField('Password', max_length=80)
    theme = models.CharField('Theme', max_length=100)
    default_style_note = models.CharField('Style', max_length=300)


class Notes(models.Model):
    """Notes"""
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, verbose_name='User', on_delete=models.SET_NULL, null=True)
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Text')
    files = models.FileField('File', upload_to='user_files/')
    style = models.CharField(
        'Style',
        max_length=300,
        default=User.objects.all.get(user_id).default_style_note
    )
    remind = models.DateTimeField('Remind', default=models.SET_NULL, null=True)
    deadline = models.DateTimeField('Remind', default=models.SET_NULL, null=True)
    done = models.BooleanField('Done', default=False)
    draft = models.BooleanField('Draft', default=False)
    date_of_adding = models.DateTimeField('Remind', default=models.SET_NULL, null=True)
