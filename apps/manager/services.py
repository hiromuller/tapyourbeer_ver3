# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
import logging

def selectLatestCommentList():
    return MODELS.Comment.objects.filter().order_by('registered_date').reverse()[:20]

def selectLatestUserList():
    return MODELS.CustomUser.objects.filter().order_by('date_joined').reverse()[:50]

def selectUntouchedBrewery():
    return MODELS.Brewery.objects.filter(logo="", address=None, description=None, web=None, webshop=None)

def selectUntouchedBeer():
    return MODELS.Beer.objects.filter(photo="", style=None, description=None, ibu=None, abv=None)

def selectUntouchedVenue():
    return MODELS.Venue.objects.filter(photo="", address=None, description=None)

def deleteCommentById(id):
    try:
        MODELS.Comment.objects.get(id=id).delete()
        return True
    except:
        return False

def selectCommentListByVenue(venue):
    try:
        comment_list = MODELS.Comment.objects.filter(venue=venue.id)
        return comment_list
    except:
        return None

def selectCommentListByUser(user):
    try:
        comment_list = MODELS.Comment.objects.filter(user = user.id).order_by('registered_date').reverse()
        return comment_list
    except:
        return []

def selectUserByCommentId(id):
    try:
        comment = MODELS.Comment.objects.get(id=id)
        user = comment.user
        return user
    except:
        return None

def selectVenueById(id):
    try:
        venue = MODELS.Venue.objects.get(id=id)
        return venue
    except:
        return None

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

def is_brewery_exist(id):
    try:
        brewery = MODELS.Brewery.objects.get(id=id)
        if brewery:
            return True
        else:
            return False
    except:
        return False

def is_beer_exist(id):
    try:
        beer = MODELS.Beer.objects.get(id=id)
        if beer:
            return True
        else:
            return False
    except:
        return False

def is_venue_exist(id):
    try:
        venue = MODELS.Venue.objects.get(id=id)
        if venue:
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

def updateBreweryManagerBreweryMerge(base_brewery, merging_brewery):
    try:
        merging_brewery_manager_list = MODELS.BreweryManager.objects.filter(brewery=merging_brewery.id)
        for merging_brewery_manager in merging_brewery_manager_list:
            if not MODELS.BreweryManager.filter(brewery=base_brewery.id, user=merging_brewery_manager.user.id):
                merging_brewery_manager.brewery = base_brewery
                merging_brewery_manager.save()
            else:
                merging_brewery_manager.delete()
        return True
    except:
        return False

def updateTCBFParticipantBreweryMerge(base_brewery, merging_brewery):
    try:
        merging_TCBFParticipant_list = MODELS.TCBFParticipant.objects.filter(brewery=merging_brewery.id)
        for merging_TCBFParticipant in merging_TCBFParticipant_list:
            if not MODELS.TCBFParticipant.filter(brewery=base_brewery.id, year=merging_TCBFParticipant.year):
                merging_TCBFParticipant.brewery = base_brewery
                merging_TCBFParticipant.save()
            else:
                merging_TCBFParticipant.delete()
        return True
    except:
        return False

def updateBeerBreweryMerge(base_brewery, merging_brewery):
    try:
        MODELS.Beer.objects.filter(brewery=merging_brewery.id).update(brewery=base_brewery.id)
        return True
    except:
        return False

def deleteBreweryByBrewery(brewery):
    try:
        MODELS.Brewery.objects.get(id=brewery.id).delete()
        return True
    except:
        return False

def updateTodaystapVenueMerge(base_venue, merging_venue):
    try:
        MODELS.TodaysTap.objects.filter(venue=merging_venue.id).update(venue=base_venue.id)
        return True
    except:
        return False

def updateCommentVenueMerge(base_venue, merging_venue):
    try:
        MODELS.Comment.objects.filter(venue=merging_venue.id).update(venue=base_venue.id)
        return True
    except:
        return False

def updateVenuemanagerVenueMerge(base_venue, merging_venue):
    try:
        base_venuemanager_list = MODELS.VenueManager.objects.filter(venue=base_venue.id)
        merging_venuemanager_list = MODELS.VenueManager.objects.filter(venue=merging_venue.id)
        base_venuemanager_venue_list = []
        base_venuemanager_user_list = []

        for base_venuemanager in base_venuemanager_list:
            base_venuemanager_venue_list.append(base_venuemanager.venue)
            base_venuemanager_user_list.append(base_venuemanager.user)

        for merging_venuemanager in merging_venuemanager_list:
            if merging_venuemanager.user in base_venuemanager_user_list:
                MODELS.VenueManager.objects.get(venue=merging_venuemanager.venue.id, user=merging_venuemanager.user.id).delete()
            else:
                n = base_venuemanager_user_list.index(merging_venuemanager.user)
                MODELS.VenueManager.objects.get(venue=merging_venuemanager.venue.id, user=merging_venuemanager.user.id).update(venue=base_venuemanager_venue_list[n])

        return True
    except:
        return False

def deleteVenueByVenue(merging_venue):
    try:
        MODELS.Venue.objects.get(id=merging_venue.id).delete()
        return True
    except:
        return False
