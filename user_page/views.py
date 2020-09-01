from django.contrib.auth.views import LoginView as djLoginView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView
from .models import Note, List, User
from .forms import LoginForm, SignInForm


def userpage(request):
    return render(request, 'user_page/user_page.html')


class NotesView(View):
    """List of films"""

    def get(self, request):
        notes = Note.objects.all()
        lists = List.objects.all()
        return render(request, 'user_page/user_page.html', {'note_list': notes, 'lists_list': lists})


class LoginView(djLoginView):
    """Login"""
    template_name = 'user_page/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('notes')

    def get_success_url(self):
        return self.success_url


class SignInView(CreateView):
    """SignIn"""
    model = User
    template_name = 'user_page/signin.html'
    form_class = SignInForm
    success_url = reverse_lazy('notes')
    success_msg = 'Success'
