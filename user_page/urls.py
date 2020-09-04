from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('add_note/<slug:username>/', views.AddNoteView.as_view(), name='add_note'),
    path('add_list/<slug:username>/', views.AddListView.as_view(), name='add_list'),
    path('add_project/<slug:username>/', views.AddProjectView.as_view(), name='add_project'),
]
