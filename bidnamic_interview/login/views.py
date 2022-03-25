from django.shortcuts import render

# import LoginView
from django.contrib.auth.views import LoginView

# import reverse_lazy
from django.urls import reverse_lazy


class Login(LoginView):
    template_name = 'login/signin.html'
    redirect_authenticated_user = True
