# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
import logging

def deleteCommentById(id):
    try:
        MODELS.Comment.objects.get(id=id).delete()
        return True
    except:
        return False

def selectBeerById(id):
    try:
        beer = MODELS.Beer.objects.get(id=id)
        return beer
    except:
        return None

def selectBreweryById(id):
    try:
        brewery = MODELS.Brewery.objects.get(id=id)
        return brewery
    except:
        return None

def is_beer_exist(id):
    try:
        beer = MODELS.Beer.objects.get(id=id)
        if beer:
            return True
        else:
            return False
    except:
        return False

def deleteBeerTasteAvgByBeer(beer):
    try:
        MODELS.BeerTasteAvg.objects.get(beer=beer.id).delete()
        return True
    except:
        return False

def deleteBeerByBeer(beer):
    try:
        MODELS.Beer.objects.get(id=beer.id).delete()
        return True
    except:
        return False


def updateCommentBeerMerge(base_beer, merging_beer):
    try:
        MODELS.Comment.objects.filter(beer=merging_beer.id).update(beer=base_beer.id)
        return True
    except:
        return False

def updateTodaystapBeerMerge(base_beer, merging_beer):
    try:
        MODELS.TodaysTap.objects.filter(beer=merging_beer.id).update(beer=base_beer.id)
        return True
    except:
        return False
