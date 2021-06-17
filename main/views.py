from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.views.generic.base import View
from .forms import SignUpForm, LogInForm
from .models import User, Settings, Style


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
        return redirect('homepage')


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
        return redirect('homepage')