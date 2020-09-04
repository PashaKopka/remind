from django import forms
from django.forms import DateInput, DateTimeInput

from .models import User, Note, List, Project
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class AddNoteForm(forms.ModelForm):
    """Note Form"""
    remind = forms.DateTimeField(required=False)
    deadline = forms.DateField(required=False)

    class Meta:
        model = Note
        fields = ('title', 'text', 'files', 'remind', 'deadline')


class AddListForm(forms.ModelForm):
    """Note Form"""
    remind = forms.DateTimeField(required=False)
    deadline = forms.DateField(required=False)

    class Meta:
        model = List
        fields = ('title', 'list', 'remind', 'deadline')


class AddProjectForm(forms.ModelForm):
    """Project Form"""
    every_day_remind = forms.DateTimeField(required=False)
    deadline = forms.DateField(required=False)

    class Meta:
        model = Project
        fields = ('title', 'every_day_remind', 'deadline')
