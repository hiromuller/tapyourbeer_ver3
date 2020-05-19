# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
import logging

logger = logging.getLogger('app')


def selectAllNewsFeedList():
    return MODELS.NewsFeed.objects.all().order_by('date').reverse()
