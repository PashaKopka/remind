from django.shortcuts import render
from django.views import View


def NotesView(request):
    return render(request=request, template_name='user_page/user_page.html')
