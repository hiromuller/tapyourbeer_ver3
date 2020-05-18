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

        if img_w >= img_h and img_h >= small_size[1]:
            new_height = small_size[1]
            new_width = new_height*aspect_ratio
        elif img_h >= img_w and img_w >= small_size[0]:
            new_width = small_size[0]
            new_height = new_width/aspect_ratio
        else:
            new_width = img_w
            new_height = img_h


        imaged = img.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        imaged.save(SETTING.MEDIA_ROOT + '/' + str(img_path), quality=100)

def resizeProfileImage(img_path):
    logger.info('resize profile image')
    if img_path:
        resizeImage(img_path)

        img_resize = Image.open(SETTING.MEDIA_ROOT + '/' + str(img_path))

        new_size = 400
        # トリミング
        center_x = int(img_resize.width / 2)
        center_y = int(img_resize.height / 2)
        img_crop = img_resize.crop((center_x - new_size / 2, center_y - new_size / 2, center_x + new_size / 2, center_y + new_size / 2))
        img_crop.save(SETTING.MEDIA_ROOT + '/' + str(img_path), quality=100)
        
