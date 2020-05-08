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
        comment_list = MODELS.Comment.objects.filter(venue=venue.id)
        return comment_list
    except:
        return None
