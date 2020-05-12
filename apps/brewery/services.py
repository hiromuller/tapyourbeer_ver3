# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
from operator import attrgetter
import logging
import pprint

logger = logging.getLogger('app')

def selectBreweryById(id):
    try:
        brewery = MODELS.Brewery.objects.get(id=id)
        return brewery
    except:
        return None

def selectBeerlistByBrewery(brewery):
    try:
        beer_list = MODELS.Beer.objects.filter(brewery=brewery.id)
        return beer_list
    except:
        return None

def selectCommentListByBeer(beer):
    try:
        comment_list = MODELS.Comment.objects.filter(beer=beer.id).order_by('registered_date').reverse()
        return comment_list
    except:
        return None

def selectCommentListByBrewery(brewery):
    try:
        beer_list = selectBeerlistByBrewery(brewery)
        comment_list = []
        for beer in beer_list:
            comment_list.extend(selectCommentListByBeer(beer))
            if len(comment_list) > 20:
                break
        comment_list = sorted(comment_list, key=attrgetter('registered_date'), reverse=True)
        comment_list = comment_list[:20]
        return comment_list
    except:
        return []

def selectVenueListByBrewery(brewery):
    try:
        comment_list = selectCommentListByBrewery(brewery)
        venue_list = []
        for comment in comment_list:
            if comment.venue:
                venue_list.append(comment.venue)
        venue_list = list(set(venue_list))
        return venue_list
    except:
        return None
