# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
from operator import attrgetter
import logging

logger = logging.getLogger('app')

#本人
def selectCustomuserbyCustomuserID(id):
    try:
        customuser = MODELS.CustomUser.objects.get(id=id)
        return customuser
    except:
        return None

#フォローしてるユーザ
def selectFollowlistbyCustomuser(customuser):
    try:
        following_list = MODELS.Follow.objects.filter(user=customuser.id)
#        print(following_list)
        return following_list
    except:
        return None

#def selectCustomuserbyFollowID(follow):
#    try:
#        customuser = MODELS.CustomUser.objects.get(id=follow_id)
#        return customuser
#    except:
#        return None

def selectFollowuserbyFollowuserID(customuser):
    try:
        following = selectFollowlistbyCustomuser(customuser)
#        print(following)
        follow_list = []
        for follow in following:
            if follow.follow:
                follow_list.append(follow.follow)
        print(follow_list)
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
        follow_list = selectFollowuserbyFollowuserID(customuser)
        comment_list = []
        for follow in follow_list:
            comment_list.extend(selectCommentbyFollow(follow))
        print(comment_list)
        comment_list = sorted(comment_list, key=attrgetter('registered_date'), reverse=True)
        return comment_list
    except:
        return None


#def selectFollowinguser(follow):
#    try:
#        followinguser_list = MODELS.CustomUser.objects.get(id=follow.follow)
#        return followinguser_list
#    except:
#        return None

#def selectFollowinguserbyCustomuserID(customuser):
#    try:
#        followinguser_list = []
#        followinguser = selectFollowinguser(follow)
#        for following in followinguser
#            followinguser_list.get(follow_id=)
#
#        return followinguser_list
#    except:
#        return []
#
#def selectCustomuserbyFollowinguserID(customUser):
#    try:


#def selectCustomuserbyFollowinguserID(customuser):
#    try:
#        customuser_list = []

#def selectCommentlistbyCustomuser(follow):
#    try:
#        comment_list = MODELS.Comment.objects.filter(user=follow.follow_id)
#        return comment_list
#    except:
#        return None

#def selectCommentlistbyFollowinguser(follow):
#    try:
#        commentlistbycustomuser = selectCommentlistbyCustomuser(follow)
#        comment_list = []
#        for comment in commentlistbycustomuser
#            commentlist.extend()
