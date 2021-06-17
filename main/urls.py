from django.urls import path
from . import views
from .views import SignUpView, LogInView, NotesView, LogOutView, ListsView, ProjectsView, TrashView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),

    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('sign_up_user/', SignUpView.as_view(), name='sign_up_user'),

    path('log_in/', LogInView.as_view(), name='log_in'),
    path('log_in_user/', LogInView.as_view(), name='log_in_user'),

    path('log_out/', LogOutView.as_view(), name='log_out'),

    path('user_page/notes/', NotesView.as_view(), name='user_page_notes'),
    path('user_page/lists/', ListsView.as_view(), name='user_page_lists'),
    path('user_page/projects/', ProjectsView.as_view(), name='user_page_projects'),
    path('user_page/trash/', TrashView.as_view(), name='user_page_trash'),
]
