from django.contrib.auth.models import User as StandartUser
from django.db import models


class User(models.Model):
    """User Model"""
    id = models.AutoField(primary_key=True)
    login = models.CharField('Login', max_length=100)
    email = models.CharField('Login', max_length=100)
    password = models.CharField('Password', max_length=80)
    theme = models.CharField('Theme', max_length=100)
    default_style_note = models.CharField('Style', max_length=300)

    def __str__(self):
        return f"{self.login}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Pocketbook:
    """Notes and Lists"""
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, to_field='id', verbose_name='User', on_delete=models.SET_NULL, null=True)
    title = models.CharField('Title', max_length=100)
    style = models.CharField(
        'Style',
        max_length=300,
        default=user_id
    )
    remind = models.DateTimeField('Remind', default=models.SET_NULL, null=True)
    deadline = models.DateTimeField('Remind', default=models.SET_NULL, null=True)
    done = models.BooleanField('Done', default=False)
    draft = models.BooleanField('Draft', default=False)
    date_of_adding = models.DateTimeField('Remind', default=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title}"


class Note(models.Model, Pocketbook):
    """Note"""
    text = models.TextField('Text')
    files = models.FileField('File', upload_to='user_files/')

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"


class List(models.Model, Pocketbook):
    """List"""
    list = models.TextField('List')

    class Meta:
        verbose_name = "List"
        verbose_name_plural = "Lists"


class Project(models.Model):
    """Project"""
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, verbose_name='User', on_delete=models.SET_NULL, null=True)
    title = models.CharField('Title', max_length=100)
    note_id = models.ManyToManyField(Note, verbose_name='Note')
    list_id = models.ManyToManyField(List, verbose_name='List')
    style = models.CharField('Style', max_length=300)
    every_day_remind = models.TimeField('EveryDayRemind', default=models.SET_NULL, null=True)
    deadline = models.DateTimeField('Remind', default=models.SET_NULL, null=True)
    done = models.BooleanField('Done', default=False)
    draft = models.BooleanField('Draft', default=False)
    date_of_adding = models.DateTimeField('Remind', default=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user_id} - {self.title}"

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
