from django.contrib import admin
from .models import User, Project, Note, List


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Notes"""
    # list_display = ("name", "age", 'get_image')
    # readonly_fields = ('style',)


admin.site.register(User)
admin.site.register(Project)
admin.site.register(List)
