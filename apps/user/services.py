# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
import logging

logger = logging.getLogger('app')

def updateUser(user):
    try:
        user.save()
        return user
    except:
        return None
        

def selectUserById(id):
    try:
        user = MODELS.CustomUser.objects.get(id=id)
        return user
    except:
        user = MODELS.CustomUser()
        user.id = 0
        user.username = '存在しません'
        return user

def selectCommentListByUser(user):
    try:
        comment_list = MODELS.Comment.objects.filter(user = user.id).order_by('registered_date').reverse()
        return comment_list
    except:
        return []
