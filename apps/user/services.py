# -*- coding: utf-8 -*-
import os
import common.models as MODELS
import common.services as COMMON_SERVICES
from django.db import transaction
from django.db.models import Q
from decimal import Decimal
from core import settings as SETTING
from core import messages as MSGS
import logging

#最大SQL発行数
MAX_SEARCH = 201
#誤差範囲
DIFF_POINT = 4/(MAX_SEARCH+1)

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

def selectCommentById(id):
    try:
        return MODELS.Comment.objects.get(id = id)
    except:
        return None

def selectCommentListByBeerExcludeTargetComment(beer, comment):
    try:
        query_result_list = MODELS.Comment.objects.filter(beer=beer.id).order_by('registered_date').reverse()
        comment_list = []
        for query_result in query_result_list:
            if not query_result == comment:
                comment_list.append(query_result)
        return comment_list
    except:
        return []


def selectCommentListByUser(user):
    try:
        comment_list = MODELS.Comment.objects.filter(user = user.id).order_by('registered_date').reverse()
        return comment_list
    except:
        return []

class ModWish(object):
    pass

def selectItemByCategoryAndId(item_category, id):
    try:
        if item_category == 1:
            item = selectBeerById(id)
        elif item_category == 2:
            item = selectBreweryById(id)
        elif item_category == 3:
            item = selectVenueById(id)
        elif item_category == 4:
            item = selectCommentById(id)
        else:
            return None
        return item
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

def selectVenueById(id):
    try:
        venue = MODELS.Venue.objects.get(id=id)
        return venue
    except:
        return None

def selectCommentById(id):
    try:
        comment = MODELS.Comment.objects.get(id=id)
        return comment
    except:
        return None

def selectWishListByUser(user):
    try:
        wish_list = MODELS.WishList.objects.filter(user = user.id).order_by('date').reverse()

        if len(wish_list) == 0:
            wish_list = []
            wish = MODELS.WishList()
            wish.item_category = 5
            wish.item_id = MSGS.NO_WISHES
            wish_list.append(wish)
        else:
            mod_wish_list = []
            for wish in wish_list:
                mod_wish = ModWish()
                mod_wish.item_category = wish.item_category
                mod_wish.item = selectItemByCategoryAndId(wish.item_category, wish.item_id)
                mod_wish.date = wish.date
                if mod_wish.item:
                    mod_wish_list.append(mod_wish)

            wish_list = mod_wish_list

        return wish_list
    except:

        wish_list = []
        wish = MODELS.WishList()
        wish.item_category = 5
        wish.item_id = MSGS.NO_WISHES
        wish_list.append(wish)
        return wish_list

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

def selectRandomBeerPhotoByBeer(beer):
    comment_list = MODELS.Comment.objects.filter(beer=beer.id).order_by('?')[:1]
    if comment_list:
        photo = comment_list[0].photo
    else:
        photo = None
    return photo

def selectSimilarBeer(keys):
    beer_taste_avg_list = []

    #検索条件を初期化
    condition_overall = Q()
    condition_bitterness = Q()
    condition_aroma = Q()
    condition_body = Q()
    condition_drinkability = Q()
    condition_pressure = Q()
    condition_specialness = Q()

    for i in range(MAX_SEARCH):
        #検索の範囲
        absolute_value = Decimal(0.5/(MAX_SEARCH - 1) * i).quantize(Decimal("0.01"))

        #検索条件設定
        if keys.get('overall') != 0:
            condition_overall = Q(overall__range=(keys['overall']-absolute_value, keys['overall']+absolute_value))
        if keys.get('bitterness') != 0:
            condition_bitterness = Q(bitterness__range=(keys['bitterness']-absolute_value, keys['bitterness']+absolute_value))
        if keys.get('aroma') != 0:
            condition_aroma = Q(aroma__range=(keys['aroma']-absolute_value, keys['aroma']+absolute_value))
        if keys.get('body') != 0:
            condition_body= Q(body__range=(keys['body']-absolute_value, keys['body']+absolute_value))
        if keys.get('drinkability') != 0:
            condition_drinkability = Q(drinkability__range=(keys['drinkability']-absolute_value, keys['drinkability']+absolute_value))
        if keys.get('pressure') != 0:
            condition_pressure = Q(pressure__range=(keys['pressure']-absolute_value, keys['pressure']+absolute_value))
        if keys.get('specialness') != 0:
            condition_specialness = Q(specialness__range=(keys['specialness']-absolute_value, keys['specialness']+absolute_value))

        result_list = MODELS.BeerTasteAvg.objects.filter(condition_overall & condition_bitterness & condition_aroma & condition_body & condition_drinkability & condition_pressure & condition_specialness).order_by('?')

        beer_taste_avg_list.extend(result_list)
        beer_taste_avg_list = sorted(set(beer_taste_avg_list), key=beer_taste_avg_list.index)

        if len(beer_taste_avg_list) >= 10:
            break

    beer_list = []
    for beer_taste_avg in beer_taste_avg_list:
        beer_list.append(beer_taste_avg.beer)

    return beer_list
