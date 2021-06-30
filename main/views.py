from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.views.generic.base import View
from .forms import SignUpForm, LogInForm, NoteForm
from .models import User, Settings, Style, File, Note


# Homepage


class HomePageView(View):

    def get(self, request):
        return render(request, 'main/homepage.html')


# User actions views

class SignUpView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'main/sign_up.html', {'sign_up_form': form})

    def post(self, request):
        form = SignUpForm(request.POST)

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if form.is_valid():
            settings = Settings.objects.create()
            style = Style.objects.get(title='default')
            settings.default_theme.set([style])
            User.objects.create_user(username=username, email=email, password=password, settings=settings)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user.last_login = now()
                login(request, user)
        return redirect('user_page_notes')


class LogInView(View):

    def get(self, request):
        form = LogInForm()
        return render(request, 'main/log_in.html', {'log_in_form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user.last_login = now()
            login(request, user)
        return redirect('user_page_notes')


class LogOutView(View):

    def get(self, request):
        logout(request)
        return redirect('homepage')


# User pages

class NotesView(View):

    def get(self, request):
        username = request.user.username
        user = User.objects.get(username=username)
        notes = user.notes.all()
        return render(request, 'main/notes.html', {'notes': notes})

    def post(self, request):
        user = User.objects.get(username=request.user.username)

        form = NoteForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            text = request.POST['text']
            if 'edit' in request.POST:
                note = Note.objects.get(id=request.POST['id'])
                note.title = title
                note.text = text
                note.save()
            else:
                note = Note.objects.create(title=title, text=text)
                if request.FILES:
                    for input_file in request.FILES.getlist('files'):
                        file = File.create_file(input_file=input_file)
                        note.files.add(file)

                user.notes.add(note)

        return redirect('user_page_notes')


class ListsView(View):

    def get(self, request):
        return render(request, 'main/lists.html')


class ProjectsView(View):

    def get(self, request):
        return render(request, 'main/projects.html')


class TrashView(View):

    def get(self, request):
        return render(request, 'main/trash.html')
