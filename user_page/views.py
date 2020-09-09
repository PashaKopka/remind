from datetime import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView as djLoginView
from django.contrib.auth.views import LogoutView as djLogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView
from .models import Note, List, User, Project
from .forms import LoginForm, SignInForm, AddNoteForm, AddListForm, AddProjectForm, EditNoteForm


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
        if form.is_valid():
            form = form.save(commit=False)
            form.user = User.objects.get_by_natural_key(username=username)
            form.save()
        return redirect('profile')


class EditNoteView(View):
    """Add List"""

    def post(self, request):
        form = EditNoteForm(request.POST)
        id = request.POST['id']
        print('\n', form.errors, '\n')
        note = Note.objects.get(id=id)
        note.title = request.POST['title']
        note.text = request.POST['text']
        note.save()

        return redirect('profile')


class AddListView(View):
    """Add List"""

    def post(self, request, username):
        form = AddListForm(request.POST)
        print('\n', form.errors, '\n')
        if form.is_valid():
            form = form.save(commit=False)
            form.user = User.objects.get_by_natural_key(username=username)
            form.save()
        return redirect('profile')


class ProjectsView(View):
    """List of projects"""

    def get(self, request):
        user = request.user
        projects = Project.objects.filter(user=user)
        notes = Note.objects.filter(user=user)
        lists = List.objects.filter(user=user)
        return render(request, 'user_page/projects_list.html',
                      {'projects_list': projects, 'note_list': notes, 'lists_list': lists})


class AddProjectView(View):
    """Add List"""

    def post(self, request, username):
        form = AddProjectForm(request.POST)
        print('\n', form.errors, '\n')
        if form.is_valid():
            form = form.save(commit=False)
            form.user = User.objects.get_by_natural_key(username=username)
            # form.note = Note.objects.get(id=notes_list)
            # form.list = List.objects.get(id=lists_list)
            form.save()

            for note_id in request.POST['note_id'].split(' '):
                if note_id != '':
                    form.note.add(Note.objects.get(id=int(note_id)))

            for list_id in request.POST['list_id'].split(' '):
                if list_id != '':
                    form.list.add(List.objects.get(id=int(list_id)))

        return redirect('projects')


class ProjectDetailView(View):
    """Project View"""

    def get(self, request, id):
        project = Project.objects.get(id=id)
        return render(request, 'user_page/project_detail.html', {'project': project})
