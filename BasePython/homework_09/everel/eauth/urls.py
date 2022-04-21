from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

import eauth.views as eauth


app_name = "eauth"

urlpatterns = [
    path('register/', eauth.UserCreateView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]