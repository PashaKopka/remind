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
        """
        Function create user and login it
        :param request: request object
        :return: redirect to user page
        """
        form = SignUpForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if form.is_valid():
            settings = self.create_default_user_settings()
            User.objects.create_user(username=username, email=email, password=password, settings=settings)
            self.authenticate_user(request, username, password)
        return redirect('user_page_notes')

    @staticmethod
    def authenticate_user(request, username, password):
        """
        Function authenticate user and login
        :param request: request object
        :param username: username
        :param password: user password
        :return: None
        """
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user.last_login = now()
            login(request, user)

    @staticmethod
    def create_default_user_settings():
        """
        Function create default user settings and theme
        :return: Settings object
        """
        settings = Settings.objects.create()
        style = Style.objects.get(title='default')
        settings.default_theme.set([style])
        return settings


class LogInView(View):

    def get(self, request):
        form = LogInForm()
        return render(request, 'main/log_in.html', {'log_in_form': form})

    def post(self, request):
        """
        Function log in user and redirect to user page
        :param request: request object
        :return: redirect to user page
        """
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
        """
        Function create new note or update existing note
        New note adding to user note m2m relationship
        :param request: request object
        :return: redirect to user page
        """
        user = User.objects.get(username=request.user.username)
        form = NoteForm(request.POST)

        if form.is_valid():
            id, title, text, files_list = self.get_request_data(request)
            if 'edit' in request.POST:
                self.update_existing_note(request, id, title, text, files_list)
            else:
                note = Note.objects.create(title=title, text=text)
                self.add_files_to_note(request, note, files_list)
                user.notes.add(note)

        return redirect('user_page_notes')

    def update_existing_note(self, request, id, title, text, files_list):
        """
        Function update existing note and save changes
        :param id: id of Note object
        :param title: new title
        :param text: new text
        :return: None
        """
        note = Note.objects.get(id=id)
        note.title = title
        note.text = text
        self.add_files_to_note(request, note, files_list)
        note.save()

    @staticmethod
    def add_files_to_note(request, note, files_list):
        """
        Function adding files to note
        :param request: request object
        :param note: Note object
        :param files_list: list of user files
        :return: None
        """
        if request.FILES:
            for input_file in files_list:
                file = File.create_file(input_file=input_file)
                note.files.add(file)

    @staticmethod
    def get_request_data(request):
        """
        Function get data from request.POST object and return it
        :param request: request object
        :return: id of note, title of note, text of note, list of user files
        """
        title = request.POST['title']
        text = request.POST['text']
        id = request.POST['id']
        files_list = request.FILES.getlist('files') if request.FILES else None

        return id, title, text, files_list


class ListsView(View):

    def get(self, request):
        return render(request, 'main/lists.html')


class ProjectsView(View):

    def get(self, request):
        return render(request, 'main/projects.html')


class TrashView(View):

    def get(self, request):
        return render(request, 'main/trash.html')
