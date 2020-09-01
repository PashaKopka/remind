from datetime import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView as djLoginView
from django.contrib.auth.views import LogoutView as djLogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView
from .models import Note, List, User
from .forms import LoginForm, SignInForm, AddNoteForm


class ProfileView(View):
    """List of films"""

    def get(self, request):
        user = request.user
        notes = Note.objects.filter(user=user)
        lists = List.objects.filter(user=user)
        return render(request, 'user_page/user_page.html', {'note_list': notes, 'lists_list': lists})


class LoginView(djLoginView):
    """Login"""
    template_name = 'user_page/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('profile')

    def get_success_url(self):
        return self.success_url


class SignInView(CreateView):
    """SignIn"""
    model = User
    template_name = 'user_page/signin.html'
    form_class = SignInForm
    success_url = reverse_lazy('profile')
    success_msg = 'Success'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class LogoutView(djLogoutView):
    next_page = reverse_lazy('login')


class AddNoteView(View):
    """Add Note"""

    def post(self, request, username):
        form = AddNoteForm(request.POST)
        print('\n', form.errors, '\n')
        print(User.objects.all())
        if form.is_valid():
            print('net')
            form = form.save(commit=False)
            form.user = User.objects.get_by_natural_key(username=username)
            form.save()
        return redirect('profile')
