# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
import logging

logger = logging.getLogger('app')

#    beer_list = []

def selectBreweryById(id):
    try:
        brewery = MODELS.Brewery.objects.get(id=id)
        return brewery
    except:
        return None

def selectBeerlistByBrewery(brewery):
    try:

        print(brewery.id)

        beer_list = MODELS.Beer.objects.filter(brewery=brewery.id)
#       beer_list = MODELS.Beer.objects.filter(brewery=brewery.id
        return beer_list
    except:
        return None

def selectCommentListByBeer(beer):
    try:
        comment_list = MODELS.Comment.objects.filter(beer=beer.id).order_by('registered_date').reverse()[0:20]
        return comment_list
    except:
        return None

def selectCommentListByBrewery(brewery):
    try:
        beer_list = selectBeerlistByBrewery(brewery)
        comment_list = []
        for beer in beer_list:
#            comment_list = selectCommentListByBeer(beer)#上書きされるからだめ
            comment_list.extend(selectCommentListByBeer(beer))
        return comment_list
    except:
        return []
