# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
import logging

logger = logging.getLogger('app')

def selectBeerById(id):
    try:
        beer = MODELS.Beer.objects.get(id=id)
        return beer
    except:
        return None

def selectBeerTasteAvgByBeer(beer):
    try:
        beer_taste_avg = MODELS.BeerTasteAvg.objects.get(beer=beer.id)
        return beer_taste_avg
    except:
        return None

def selectBreweryById(id):
    try:
        brewery = MODELS.Brewery.objects.get(id=id)
        return brewery
    except:
        return None

def selectCommentListByBeer(beer):
    try:
        comment_list = MODELS.Comment.objects.filter(beer=beer.id).order_by('registered_date').reverse()
        return comment_list
    except:
        return []

def selectVenueListByBeer(beer):
    try:
        comment_list = selectCommentListByBeer(beer)
        venue_list = []

        for comment in comment_list:
            venue = MODELS.Venue.objects.get(id=comment.venue_id)
            venue_list.append(venue)

        venue_list = set(venue_list)

        return venue_list
    except:
        return []
