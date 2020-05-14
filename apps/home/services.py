# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
from operator import attrgetter
import logging

logger = logging.getLogger('app')

def selectCustomuserbyID(id):
    try:
        customuser = MODELS.CustomUser.objects.get(id=id)
        return customuser
    except:
        return None

def selectFollowlistbyCustomuser(customuser):
    try:
        follow_list = MODELS.Follow.objects.filter(user=customuser.id)
        return follow_list
    except:
        return None

def selectFollowuserbyFollowuser(customuser):
    try:
        following = selectFollowlistbyCustomuser(customuser)
        follow_list = []
        for follow in following:
            if follow.follow:
                follow_list.append(follow.follow)
        return follow_list
    except:
        return None

def selectCommentbyFollow(follow):
    try:
        comment = MODELS.Comment.objects.filter(user=follow)
        return comment
    except:
        return None

def selectCommentlistbyCustomuser(customuser):
    try:
        follow_list = selectFollowuserbyFollowuser(customuser)
        comment_list = []
        for follow in follow_list:
            comment_list.extend(selectCommentbyFollow(follow))
        comment_list = sorted(comment_list, key=attrgetter('registered_date'), reverse=True)
        return comment_list
    except:
        return None
