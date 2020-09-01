from django.contrib import admin
from .models import User, Project, Note, List


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Notes"""
    # list_display = ("name", "age", 'get_image')
    # readonly_fields = ('style',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Notes"""
    # readonly_fields = ('id', 'username', 'email', 'password',)
    # list_display = ('theme', 'default_style_note')


admin.site.register(Project)
admin.site.register(List)
