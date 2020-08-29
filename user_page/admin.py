from django.contrib import admin
from .models import User, Project, Note, List

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Note)
admin.site.register(List)
