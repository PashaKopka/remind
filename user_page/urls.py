from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesView, name='notes')
]
