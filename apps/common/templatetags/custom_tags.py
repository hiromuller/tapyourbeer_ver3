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

@register.filter(name='length_over_50')
def length_over_50(list):
    count = len(list)
    if count > 50:
        return True
    else:
        return False
