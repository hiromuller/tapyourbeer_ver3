# -*- coding: utf-8 -*-
import os
import common.models as MODELS
import common.services as COMMON_SERVICES
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

def updateUser(form, user, previous_photo):
    try:
        if form.is_valid():
            form.save()
            if user.photo:
                COMMON_SERVICES.resizeProfileImage(user.photo)
            if previous_photo:
                if previous_photo != 'images/' + str(user.photo):
                    os.remove(SETTING.MEDIA_ROOT + '/' + str(previous_photo))
    except:
        return

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

def selectFollowListByUser(user):
    try:
        follow_list = MODELS.Follow.objects.filter(user=user.id)
        return follow_list
    except:
        return []

def selectFollowerListByUser(user):
    try:
        follower_list = MODELS.Follow.objects.filter(follow=user.id)
        return follower_list
    except:
        return []

def getNumFollower(user):
    return MODELS.Follow.objects.filter(follow=user.id).count()

def getNumFollow(user):
    return MODELS.Follow.objects.filter(user=user.id).count()
