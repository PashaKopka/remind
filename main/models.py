from django.db import models as m
from django.contrib.auth.models import User as djUser
from django.utils.timezone import now


class File(m.Model):
    file = m.FileField(upload_to='uploads/%Y/%m/%d', blank=False)
    datetime = m.DateTimeField(default=now())

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'


class Style(m.Model):
    background = m.CharField(max_length=50)
    font_color = m.CharField(max_length=50)
    font_size = m.IntegerField()
    font_width = m.IntegerField()
    border_radius = m.IntegerField()
    border_color = m.CharField(max_length=50)

    class Meta:
        verbose_name = 'Style'
        verbose_name_plural = 'Styles'


class Notification(m.Model):
    title = m.CharField(max_length=50, blank=False)
    text = m.CharField(max_length=50, blank=True)
    date = m.DateField(verbose_name='date_of_notification', blank=True)
    time = m.TimeField(verbose_name='time_of_notification', blank=False)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'


class ListElement(m.Model):
    text = m.CharField(max_length=50, blank=False)
    done = m.BooleanField(default=False)
    file = m.ManyToManyField(File, blank=True)

    class Meta:
        verbose_name = 'List element'
        verbose_name_plural = 'List elements'


class AbstractRemind(m.Model):
    style = m.ManyToManyField(Style, blank=False)
    date_of_creation = m.DateField(verbose_name='date_of_creation_remind', default=now(), blank=False)
    date_of_change = m.DateField(verbose_name='date_of_changing_remind', blank=True)
    draft = m.BooleanField()

    class Meta:
        abstract = True


class Note(AbstractRemind):
    title = m.CharField(max_length=50, blank=True)
    text = m.TextField(blank=False)
    files = m.ManyToManyField(File, blank=True)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'


class List(AbstractRemind):
    title = m.CharField(max_length=50, blank=True)
    list_elements = m.ManyToManyField(ListElement, related_name='elements_of_this_list')
    notification = m.ManyToManyField(Notification, related_name='notification')

    class Meta:
        verbose_name = 'List'
        verbose_name_plural = 'Lists'


class Project(AbstractRemind):
    title = m.CharField(max_length=50, blank=False)
    notes = m.ManyToManyField(Note)
    lists = m.ManyToManyField(List)
    time_of_notification = m.ManyToManyField(Notification, related_name='time_of_notification', blank=True)
    deadline = m.ManyToManyField(Notification, related_name='deadline', blank=False)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Settings(m.Model):
    default_theme = m.ManyToManyField(Style)

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'


class User(djUser):
    notes = m.ManyToManyField(Note, related_name='user_notes')
    lists = m.ManyToManyField(List, related_name='user_lists')
    projects = m.ManyToManyField(Project, related_name='user_projects')
    settings = m.ForeignKey(Settings, related_name='user_settings', on_delete=m.CASCADE)

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            last_login=now(),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
