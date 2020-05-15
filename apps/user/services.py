# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
import logging

logger = logging.getLogger('app')

def followFriend(user, follow):
    try:
        followModel = MODELS.Follow()
        followModel.user = user
        followModel.follow = follow
        followModel.save()
        return True
    except:
        return None

def unfollowFriend(user, follow):
    try:
        followModel = MODELS.Follow.objects.get(user=user.id, follow=follow.id)
        followModel.delete()
        return True
    except:
        return None

def updateUser(user):
    try:
        user.save()
        return user
    except:
        return None

def isFollowing(user, follow):
    try:
        is_following = MODELS.Follow.objects.get(user=user.id, follow=follow.id)
        if is_following:
            return True
        else:
            return False
    except:
        return False

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

def getNumFollower(user):
    return MODELS.Follow.objects.filter(follow=user.id).count()

def getNumFollow(user):
    return MODELS.Follow.objects.filter(user=user.id).count()
