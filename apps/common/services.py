# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from core import settings as SETTING
import logging
import jaconv

def normalizeStr(str):
    str = jaconv.normalize(str, 'NFKC')
    str = jaconv.z2h(str, digit=True, ascii=True, kana=False)
    str = jaconv.h2z(str, digit=False, ascii=False, kana=True)
    str = str.upper()
    return str
