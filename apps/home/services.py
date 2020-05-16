# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
from operator import attrgetter
from django.db.models import Q
import logging

logger = logging.getLogger('app')

def selectCustomuserbyID(id):
    try:
        customuser = MODELS.CustomUser.objects.get(id=id)
        return customuser
    except:
        return None

def selectFollowUserLisybyFollowuser(id):
    try:
        follow_list = MODELS.Follow.objects.filter(user=id)
        follow_user_list = []
        for follow in follow_list:
            if follow.follow:
                follow_user_list.append(follow.follow)
        return follow_user_list
    except:
        return None

def selectCommentListbyFollowList(id):
    try:
        follow_user_list = selectFollowUserLisybyFollowuser(id)
        comment_list = []
        queries = [Q(user=follow) for follow in follow_user_list]
        query = queries.pop()
        for item in queries:
            query |= item
        comment_list = MODELS.Comment.objects.filter(query).order_by('-registered_date')[:30]
        return comment_list
    except:
        return None
