# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
import logging

def deleteCommentById(id):
    try:
        MODELS.Comment.objects.get(id=id).delete()
        return
    except:
        return
