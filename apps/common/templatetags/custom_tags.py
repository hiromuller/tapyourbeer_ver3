# -*- coding: utf-8 -*-
import common.models as MODELS
from django import template

register = template.Library()

@register.filter(name='make_range')
def make_range(value):
    try:
        if value:
            return range(round(value))
        else:
            return range(0)
    except:
        return range(0)

@register.filter(name='get_like_count')
def get_like_count(comment_id):
    try:
        count = len(MODELS.Like.objects.filter(comment=comment_id))
        return count
    except Exception as e:
        return 0

@register.filter(name='is_liked')
def is_liked(comment_id, user_id):
    try:
        if len(MODELS.Like.objects.filter(comment=comment_id, user=user_id)) == 0:
            return False
        else:
            return True
    except Exception as e:
        return False

@register.filter(name='get_comment_wish_count')
def get_comment_wish_count(comment_id):
    try:
        count = len(MODELS.WishList.objects.filter(item_category=4, item_id=comment_id))
        return count
    except Exception as e:
        return 0

@register.filter(name='comment_is_wished')
def comment_is_wished(comment_id, user_id):
    try:
        if len(MODELS.WishList.objects.filter(item_category=4, item_id=comment_id, user=user_id)) == 0:
            return False
        else:
            return True
    except Exception as e:
        return False

@register.filter(name='beer_is_wished')
def beer_is_wished(beer_id, user_id):
    try:
        if len(MODELS.WishList.objects.filter(item_category=1, item_id=beer_id, user=user_id)) == 0:
            return False
        else:
            return True
    except Exception as e:
        return False

@register.filter(name='brewery_is_wished')
def brewery_is_wished(brewery_id, user_id):
    try:
        if len(MODELS.WishList.objects.filter(item_category=2, item_id=brewery_id, user=user_id)) == 0:
            return False
        else:
            return True
    except Exception as e:
        return False

@register.filter(name='venue_is_wished')
def venue_is_wished(venue_id, user_id):
    try:
        if len(MODELS.WishList.objects.filter(item_category=3, item_id=venue_id, user=user_id)) == 0:
            return False
        else:
            return True
    except Exception as e:
        return False

@register.filter(name='length_over_50')
def length_over_50(list):
    count = len(list)
    if count > 50:
        return True
    else:
        return False

@register.filter(name='int_over_50')
def int_over_50(int):
    if int > 50:
        return True
    else:
        return False
