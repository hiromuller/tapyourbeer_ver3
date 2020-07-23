# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
import logging

def selectVenueById(id):
    try:
        venue = MODELS.Venue.objects.get(id=id)
        return venue
    except:
        return None

def selectCommentListByVenue(venue):
    try:
        comment_list = MODELS.Comment.objects.filter(venue=venue.id).order_by('registered_date').reverse()[:30]
        return comment_list
    except:
        return None

def selectBeerListByVenue(venue):
    try:
        beer_id_list = MODELS.Comment.objects.filter(venue=venue.id).values_list('beer', flat=True).distinct()
        beer_list = []
        for beer_id in beer_id_list:
            beer_list.append(MODELS.Beer.objects.get(id=beer_id))
        return beer_list
    except:
        return None

def selectBreweryListByBeerList(beer_list):
    try:
        brewery_list = []
        for beer in beer_list:
            if not beer.brewery in brewery_list:
                brewery_list.append(beer.brewery)
        return brewery_list
    except:
        return None
