from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),

    # User actions
    path('login/', views.LoginView.as_view(), name='login'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # Notes
    path('add_note/<slug:username>/', views.AddNoteView.as_view(), name='add_note'),
    path('edit_note/', views.EditNoteView.as_view(), name='edit_note'),
    path('', views.ProfileView.as_view(), name='search_note'),
    path('del', views.DelNoteView.as_view(), name='note_del'),

    # Lists
    path('add_list/<slug:username>/', views.AddListView.as_view(), name='add_list'),
    path('lists/', views.ListView.as_view(), name='lists'),
    path('edit_list/', views.EditListView.as_view(), name='edit_list'),
    path('lists/check', views.CheckListView.as_view(), name='check_list'),
    path('lists/del', views.DelListView.as_view(), name='list_del'),

    # Projects
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('project_detail/<int:id>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('add_project/<slug:username>/', views.AddProjectView.as_view(), name='add_project'),
]
