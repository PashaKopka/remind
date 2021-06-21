from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models as m
from django.contrib.auth.models import User as djUser
from django.utils.timezone import now
from PIL import Image, UnidentifiedImageError

from remind.settings import BASE_DIR, FILE_FORMATS, DEFAULT_FILE_ICON


class File(m.Model):
    filename = m.CharField(max_length=150, default='file')
    file = m.FileField(upload_to='uploads/%Y/%m/%d', blank=False)
    icon = m.CharField(max_length=100, default=DEFAULT_FILE_ICON)
    datetime = m.DateTimeField(default=now())

    @staticmethod
    def create_file(input_file: InMemoryUploadedFile):
        file_format = input_file.name.split('.')[-1]
        icon = DEFAULT_FILE_ICON
        if file_format in FILE_FORMATS:
            icon = FILE_FORMATS[file_format]
        file = File.objects.create(
            filename=input_file.name,
            file=input_file,
            icon=icon
        )

        return file

    def is_image(self):
        try:
            Image.open(BASE_DIR.__str__() + self.file.url)
        except UnidentifiedImageError:
            return False
        return True

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'


class Style(m.Model):
    title = m.CharField(max_length=50, default='')
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
    date_of_change = m.DateField(verbose_name='date_of_changing_remind', blank=True, null=True)
    draft = m.BooleanField(default=False)

    class Meta:
        abstract = True


class Note(AbstractRemind):
    title = m.CharField(max_length=50, blank=True)
    text = m.TextField(blank=False)
    files = m.ManyToManyField(File, blank=True)

    def get_files(self):
        return self.files.all()

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
    notes = m.ManyToManyField(Note, related_name='user_notes', blank=True)
    lists = m.ManyToManyField(List, related_name='user_lists', blank=True)
    projects = m.ManyToManyField(Project, related_name='user_projects', blank=True)
    settings = m.ForeignKey(Settings, related_name='user_settings', on_delete=m.CASCADE, null=True)

    def create_user(self, username, email, password, settings):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            settings=settings
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
