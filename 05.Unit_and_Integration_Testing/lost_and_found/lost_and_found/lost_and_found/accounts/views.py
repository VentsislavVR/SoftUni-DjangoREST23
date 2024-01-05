from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy


# Create your views here.
class LoginUserView(auth_views.LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')