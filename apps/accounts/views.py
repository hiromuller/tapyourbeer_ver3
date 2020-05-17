# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, authenticate
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
import accounts.forms as FORMS
import home.views as HOME_VIEWS
import logging
logger = logging.getLogger('app')

class Login(LoginView):
    """ログインページ"""
    form_class = FORMS.LoginForm
    template_name = 'common/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'common/login.html'

def signup_index(request):
    logger.info('signup')
    if request.method == 'POST':
        forms = {'SignUpForm':FORMS.SignUpForm(request.POST)}
    else:
        forms = {'SignUpForm':FORMS.SignUpForm()}
    c = {}
    main_url = CONFIG.TOP_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                }
    c.update({'html_title':CONFIG.HOME_HTML_TITLE})
    c.update(url_dict)
    c.update(forms)
    c.update(action_dict)
    return render(request, 'common/signup.html', c)

def signup_user(request):
    logger.info('signup_user')
    c = {}

    form = FORMS.SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
    else:
        return signup_index(request)

    return HOME_VIEWS.Home(request)
