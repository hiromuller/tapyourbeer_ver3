# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import consts as CONST
from core import configs as CONFIG
from core import settings as SETTING
import common.services as SERVICES
import common.models as MODELS
import home.views as HOME_VIEWS
import beer.views as BEER_VIEWS
import brewery.views as BREWERY_VIEWS
import manager.views as MANAGER_VIEWS
import search.views as SEARCH_VIEWS
import detail_search.views as DETAIL_SEARCH_VIEWS
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
    elif action == CONFIG.ACTION_SIGNUP:
        return ACCOUNTS_VIEWS.signup_index(request)
    elif action == CONFIG.ACTION_SIGNUP_USER:
        return ACCOUNTS_VIEWS.signup_user(request)
    elif action == CONFIG.ACTION_BEER_DETAIL:
        return BEER_VIEWS.beerDetail(request)
    elif action == CONFIG.ACTION_ADD_BEER_EVALUATION_FORM:
        return BEER_VIEWS.addBeerEvaluationForm(request)
    elif action == CONFIG.ACTION_ADD_BEER_EVALUATION:
        return BEER_VIEWS.addBeerEvaluation(request)
    elif action == CONFIG.ACTION_BREWERY_DETAIL:
        return BREWERY_VIEWS.breweryDetail(request)
    elif action == CONFIG.ACTION_MANAGER_ACCOUNT:
        return MANAGER_VIEWS.index(request)
    elif action == CONFIG.ACTION_SEARCH:
        return SEARCH_VIEWS.index(request)
    elif action == CONFIG.ACTION_SEARCH_LIST:
        return SEARCH_VIEWS.searchList(request)
    elif action == CONFIG.ACTION_DETAIL_SEARCH:
        return DETAIL_SEARCH_VIEWS.index(request)
    elif action == CONFIG.ACTION_DETAIL_SEARCH_LIST:
        return DETAIL_SEARCH_VIEWS.detailSearchList(request)
    elif action == CONFIG.ACTION_USER_ACCOUNT:
        return USER_VIEWS.showUser(request)
    elif action == CONFIG.ACTION_USER_UPDATE:
        return USER_VIEWS.showUserUpdate(request)
    elif action == CONFIG.ACTION_UPDATE_USER:
        return USER_VIEWS.updateUser(request)
    elif action == CONFIG.ACTION_FOLLOW:
        return USER_VIEWS.follow(request)
    elif action == CONFIG.ACTION_UNFOLLOW:
        return USER_VIEWS.unfollow(request)
    elif action == CONFIG.ACTION_VENUE_DETAIL:
        return VENUE_VIEWS.venueDetail(request)
    elif action == CONFIG.ACTION_DELETE_COMMENT:
        return MANAGER_VIEWS.deleteComment(request)
    elif action == CONFIG.ACTION_BEER_UPDATE:
        return MANAGER_VIEWS.showBeerUpdate(request)
    elif action == CONFIG.ACTION_UPDATE_BEER:
        return MANAGER_VIEWS.updateBeer(request)
    elif action == CONFIG.ACTION_BREWERY_UPDATE:
        return MANAGER_VIEWS.showBreweryUpdate(request)
    elif action == CONFIG.ACTION_UPDATE_BREWERY:
        return MANAGER_VIEWS.updateBrewery(request)
    elif action == CONFIG.ACTION_BEER_MERGE:
        return MANAGER_VIEWS.showBeerMerge(request)
    elif action == CONFIG.ACTION_MERGE_BEER:
        return MANAGER_VIEWS.mergeBeer(request)
    elif action == CONFIG.ACTION_BREWERY_MERGE:
        return MANAGER_VIEWS.showBreweryMerge(request)
    elif action == CONFIG.ACTION_MERGE_BREWERY:
        return MANAGER_VIEWS.mergeBrewery(request)
    elif action == CONFIG.ACTION_VENUE_UPDATE:
        return MANAGER_VIEWS.showVenueUpdate(request)
    elif action == CONFIG.ACTION_UPDATE_VENUE:
        return MANAGER_VIEWS.updateVenue(request)
    else:
        return view(request)

def view(request):
    return HOME_VIEWS.index(request)
