from django import forms
from django.contrib.auth import views as auth_views, login, authenticate

from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy
from django.views import generic as views
from django.utils.translation import gettext_lazy as _


# Create your views here.

# def register_user(request):
#     ...


class RegisterUserForm(auth_forms.UserCreationForm):
    consent = forms.BooleanField()

    password2 = forms.CharField(
        label=_("Repeat Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password!!!!!"),
    )


class RegisterUserView(views.CreateView):
    template_name = 'app_auth/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('register_user')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


class LoginUserView(auth_views.LoginView):
    ...


class LogoutUserView(views.View):
    ...
