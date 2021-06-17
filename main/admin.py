from django.contrib import admin
from .models import User, Note, List, ListElement, Project, Settings, Style, Notification, File


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    model = Note


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    model = List


@admin.register(ListElement)
class ListElementAdmin(admin.ModelAdmin):
    model = ListElement


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    model = Settings


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    model = Style


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    model = Notification


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    model = File
