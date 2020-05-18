# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from PIL import Image
from core import settings as SETTING
import logging
import jaconv

logger = logging.getLogger('app')


def normalizeStr(str):
    str = jaconv.normalize(str, 'NFKC')
    str = jaconv.z2h(str, digit=True, ascii=True, kana=False)
    str = jaconv.h2z(str, digit=False, ascii=False, kana=True)
    str = str.upper()
    return str


def resizeImage(img_path):
    logger.info('resize image')
    if img_path:
        small_size = (400, 400)
        img = Image.open(SETTING.MEDIA_ROOT + '/' + str(img_path))
        img_w, img_h = img.size
        aspect_ratio = img_w / float(img_h)
        new_height = int(small_size[0] / aspect_ratio)

        if new_height < 100:
            final_width = small_size[0]
            final_height = new_height
        else:
            final_width = int(aspect_ratio * small_size[1])
            final_height = small_size[1]

        imaged = img.resize((final_width, final_height), Image.ANTIALIAS)
        imaged.save(SETTING.MEDIA_ROOT + '/' + str(img_path), quality=100)
