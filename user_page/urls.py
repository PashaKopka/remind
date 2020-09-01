from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesView.as_view(), name='notes'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
