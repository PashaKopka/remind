from django.urls import path
from . import views
from .views import SignUpView, LogInView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),

    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('sign_up_user/', SignUpView.as_view(), name='sign_up_user'),

    path('log_in/', LogInView.as_view(), name='log_in'),
    path('log_in_user/', LogInView.as_view(), name='log_in_user'),
]
