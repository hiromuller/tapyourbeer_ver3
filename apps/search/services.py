# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db.models import Q
from django.db import transaction
from decimal import Decimal
from core import settings as SETTING
import logging
import random

#最大検索結果数
MAX_RESULTS = 50

def selectBeerListByNameKey(key):
    beer_list = MODELS.Beer.objects.filter(name__icontains=key, is_active=True)[:MAX_RESULTS]
    return beer_list

def selectBreweryListByNameKey(key):
    brewery_list = MODELS.Brewery.objects.filter(name__icontains=key, is_active=True)[:MAX_RESULTS]
    return brewery_list

def selectVenueListByNameKey(key):
    venue_list = MODELS.Venue.objects.filter(name__icontains=key, is_active=True)[:MAX_RESULTS]
    return venue_list

def selectUserListByUsernameKey(key):
    user_list = MODELS.CustomUser.objects.filter(username__icontains=key, is_active=True)[:MAX_RESULTS]
    return user_list
