"""
This file consisting Authentic view ,
inherited Auth view (login , and logout view)
also used LoginRequiredMixin mixins for checking user is authorized or not
"""

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, View
from .TokenGenrator import token_validator
from .forms import CreateUserForm
from .models import User


class Home(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        if self.request.user.user_type == "User":
            return render(request, template_name="index.html")
        else:
            return render(request, template_name="index.html")


class Register(CreateView):
    form_class = CreateUserForm
    success_url = "/accounts/UserLogin"
    template_name = "account.html"


class UserLogin(LoginView):
    template_name = 'index.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class UserLogout(LoginRequiredMixin, LogoutView):
    next_page = "/"


class VerifyEmail(View):

    def get(self, request, token):
        payload = token_validator(token)
        if payload:
            usr = User.objects.get(id=payload.id)
            usr.is_verified = True
            usr.save()
        return redirect("home")
