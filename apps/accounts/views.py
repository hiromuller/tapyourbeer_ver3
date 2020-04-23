from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
import accounts.forms as FORMS


class Login(LoginView):
    """ログインページ"""
    form_class = FORMS.LoginForm
    template_name = 'common/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'common/login.html'
