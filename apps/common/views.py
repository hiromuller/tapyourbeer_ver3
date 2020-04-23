# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import consts as CONST
from core import configs as CONFIG
from core import settings as SETTING
import common.services as SERVICES
import home.views as HOME_VIEWS
import beer.views as BEER_VIEWS
import brewery.views as BREWERY_VIEWS
import manager.views as MANAGER_VIEWS
import search.views as SEARCH_VIEWS
import user.views as USER_VIEWS
import venue.views as VENUE_VIEWS
import accounts.views as ACCOUNTS_VIEWS
import logging
logger = logging.getLogger('app')

def index(request):
    if request.method =="POST":
        action = request.POST["action"]
    else:
        action = CONFIG.ACTION_HOME

    print (action)

    if action == CONFIG.ACTION_HOME:
        return HOME_VIEWS.index(request)
    elif action == CONFIG.ACTION_BEER_DETAIL:
        return BEER_VIEWS.index(request)
    elif action == CONFIG.ACTION_ADD_BEER_EVALUATION:
        return BEER_VIEWS.show_add_beer_form(request)
    elif action == CONFIG.ACTION_BREWERY_DETAIL:
        return BREWERY_VIEWS.index(request)
    elif action == CONFIG.ACTION_MANAGER_ACCOUNT:
        return MANAGER_VIEWS.index(request)
    elif action == CONFIG.ACTION_SEARCH_LIST:
        return SEARCH_VIEWS.index(request)
    elif action == CONFIG.ACTION_USER_ACCOUNT:
        return USER_VIEWS.index(request)
    elif action == CONFIG.ACTION_VENUE_DETAIL:
        return VENUE_VIEWS.index(request)
    else:
        return view(request)

def view(request):
    return HOME_VIEWS.index(request)
