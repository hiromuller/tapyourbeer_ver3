# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
import logging
import jaconv

logger = logging.getLogger('app')

def deleteBeerTasteAvgByBeer(beer):
    try:
        MODELS.BeerTasteAvg.objects.get(beer=beer.id).delete()
        return True
    except:
        return False

def selectBeerById(id):
    try:
        beer = MODELS.Beer.objects.get(id=id)
        return beer
    except:
        return None

def selectBeerByNameAndBrewery(name, brewery):
    try:
        beer = MODELS.Beer.objects.get(name=name, brewery=brewery.id)
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

def selectBreweryByName(name):
    try:
        brewery = MODELS.Brewery.objects.get(name=name)
        return brewery
    except:
        return None

def selectVenueById(id):
    try:
        venue = MODELS.Venue.objects.get(id=id)
        return venue
    except:
        return None

def selectCommentListByBeer(beer):
    try:
        comment_list = MODELS.Comment.objects.filter(beer=beer.id).order_by('registered_date').reverse()
        return comment_list
    except:
        return []

def selectVenueListByName(name):
    try:
        venue_list = MODELS.Venue.objects.filter(name=name)
        return venue_list
    except:
        return False

def selectVenueListByBeer(beer):
    try:
        comment_list = selectCommentListByBeer(beer)
        venue_list = []
        for comment in comment_list:
            try:
                venue = MODELS.Venue.objects.get(id=comment.venue.id)
            except:
                continue
            venue_list.append(venue)
        venue_list = set(venue_list)
        return venue_list
    except:
        return []

def isBeerExistByNameAndBrewery(name, brewery):
    try:
        beer = MODELS.Beer.objects.get(name=name, brewery=brewery.id)
        if beer:
            return True
        else:
            return False
    except:
        return False


def isBreweryExistByName(name):
    try:
        brewery = MODELS.Brewery.objects.get(name=name)
        if brewery:
            return True
        else:
            return False
    except:
        return False

def isVenueExistByName(name):
    try:
        venue = MODELS.Venue.objects.filter(name=name)
        if venue:
            return True
        else:
            return False
    except:
        return False


def addBreweryByName(name):
    try:
        brewery = MODELS.Brewery()
        brewery.name = name
        brewery.save()
        return brewery
    except:
        return None

def addBeerByNameAndBrewery(name, brewery):
    try:
        beer = MODELS.Beer()
        beer.name = name
        beer.brewery = brewery
        beer.save()
        return beer
    except:
        return None

def addVenueByName(name):
    try:
        venue = MODELS.Venue()
        venue.name = name
        venue.save()
        return venue
    except:
        return None

def addCommentByDict(comment_dict):
    try:
        comment = MODELS.Comment()
        comment.beer = comment_dict.get('beer')
        comment.user = comment_dict.get('user')
        comment.venue = comment_dict.get('venue')
        comment.overall = comment_dict.get('overall')
        comment.bitterness = comment_dict.get('bitterness')
        comment.aroma = comment_dict.get('aroma')
        comment.body = comment_dict.get('body')
        comment.drinkability = comment_dict.get('drinkability')
        comment.pressure = comment_dict.get('pressure')
        comment.specialness = comment_dict.get('specialness')
        comment.comment = comment_dict.get('comment')
        comment.save()
        return comment

    except:
        return None
