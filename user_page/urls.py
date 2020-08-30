from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesView.as_view(), name='notes')
]
