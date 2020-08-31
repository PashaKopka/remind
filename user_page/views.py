from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Note, List


class NotesView(View):
    """List of films"""

    def get(self, request):
        notes = Note.objects.all()
        lists = List.objects.all()
        return render(request, 'user_page/user_page.html', {'note_list': notes, 'lists_list': lists})
