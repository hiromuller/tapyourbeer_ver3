# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db import transaction
from PIL import Image
from core import settings as SETTING
import logging
import jaconv
from datetime import datetime as dt
from django.utils import timezone

logger = logging.getLogger('app')


def normalizeStr(str):
    str = jaconv.normalize(str, 'NFKC')
    str = jaconv.z2h(str, digit=True, ascii=True, kana=False)
    str = jaconv.h2z(str, digit=False, ascii=False, kana=True)
    str = str.upper()
    return str


def resizeImage_venue_header(img_path):
    logger.info('resize image venue header')
    if img_path:
        new_max_width = 800
        img = Image.open(SETTING.MEDIA_ROOT + '/' + str(img_path))
        #exif情報取得
        try:
            exifinfo = img._getexif()
        except:
            exifinfo = None

        if exifinfo:
            #exif情報からOrientationの取得
            orientation = exifinfo.get(0x112, 1)
            #画像を回転
            rot_img = rotateImage(img, orientation)
        else:
            #exif情報が取得できなかった場合は、そのまま処理を続ける
            rot_img = img

        img_w, img_h = rot_img.size
        aspect_ratio = img_w / float(img_h)

        #リサイズ
        if img_w >= new_max_width:
            new_width = new_max_width
            new_height = new_width/aspect_ratio
            resized_image = rot_img.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        else:
            resized_image = rot_img

        #高さトリミング
        if resized_image.height > resized_image.width / 2:
            crop_height = resized_image.width / 2
            center_y = int(resized_image.height / 2)
            final_image = resized_image.crop((0, center_y - crop_height / 2, resized_image.width, center_y + crop_height / 2))
        else:
            final_image = resized_image

        final_image.save(SETTING.MEDIA_ROOT + '/' + str(img_path), quality=100)


def resizeImage(img_path):
    logger.info('resize image')
    if img_path:
        small_size = (400, 400)
        img = Image.open(SETTING.MEDIA_ROOT + '/' + str(img_path))
        #exif情報取得
        try:
            exifinfo = img._getexif()
        except:
            exifinfo = None
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

        if exifinfo:
            #exif情報からOrientationの取得
            orientation = exifinfo.get(0x112, 1)
            #画像を回転
            final_image = rotateImage(imaged, orientation)
        else:
            #exif情報が取得できなかった場合は、そのまま処理を続ける
            final_image = imaged

        final_image.save(SETTING.MEDIA_ROOT + '/' + str(img_path), quality=100)

        createThumbnail(img_path)

def createThumbnail(img_path):
    logger.info('create thumbnail')
    if img_path:
        img_resize = Image.open(SETTING.MEDIA_ROOT + '/' + str(img_path))

        new_size = 300
        # トリミング
        center_x = int(img_resize.width / 2)
        center_y = int(img_resize.height / 2)
        img_crop = img_resize.crop((center_x - new_size / 2, center_y - new_size / 2, center_x + new_size / 2, center_y + new_size / 2))
        img_crop.save(SETTING.MEDIA_ROOT + '/thumb_' + str(img_path), quality=100)


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

def rotateImage(img, orientation):
    """
    画像ファイルをOrientationの値に応じて回転させる
    """
    #orientationの値に応じて画像を回転させる
    if orientation == 1:
        img_rotate = img
    elif orientation == 2:
        #左右反転
        img_rotate = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 3:
        #180度回転
        img_rotate = img.transpose(Image.ROTATE_180)
    elif orientation == 4:
        #上下反転
        img_rotate = img.transpose(Image.FLIP_TOP_BOTTOM)
    elif orientation == 5:
        #左右反転して90度回転
        img_rotate = img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90)
    elif orientation == 6:
        #270度回転
        img_rotate = img.transpose(Image.ROTATE_270)
    elif orientation == 7:
        #左右反転して270度回転
        img_rotate = img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270)
    elif orientation == 8:
        #90度回転
        img_rotate = img.transpose(Image.ROTATE_90)
    else:
        img_rotate = img

    return img_rotate

def parseDate(dateData):
    return dt(
        dateData.tm_year,
        dateData.tm_mon,
        dateData.tm_mday,
        dateData.tm_hour,
        dateData.tm_min,
        dateData.tm_sec,
        tzinfo=timezone.utc
    )

def selectCommentById(id):
    try:
        return MODELS.Comment.objects.get(id=id)
    except:
        return None

def selectBeerById(id):
    try:
        return MODELS.Beer.objects.get(id=id)
    except:
        return None

def addLike(user, comment):
    try:
        like = MODELS.Like()
        like.comment = comment
        like.user = user
        like.save()
        return True
    except:
        return False

def deleteLike(user, comment):
    try:
        like = MODELS.Like.objects.get(comment=comment.id, user=user.id)
        like.delete()
        return True
    except:
        return False

def is_liked(user, comment):
    try:
        return MODELS.Like.objects.get(comment=comment.id, user=user.id)
    except:
        return False

def getLikeCount(comment):
    try:
        num = len(MODELS.Like.objects.filter(comment = comment.id))
        return num
    except:
        return 0

def comment_is_wished(user, comment):
    try:
        return MODELS.WishList.objects.get(item_category=4, item_id=comment.id, user_id=user.id)
    except:
        return False

def deleteCommentWish(user, comment):
    try:
        wish = MODELS.WishList.objects.get(item_category=4, item_id=comment.id, user_id=user.id)
        wish.delete()
        return True
    except:
        return False

def addCommentWish(user, comment):
    try:
        wish = MODELS.WishList()
        wish.item_category = 4
        wish.item_id = comment.id
        wish.user = user
        wish.save()
        return True
    except:
        return False

def getCommentWishCount(comment):
    try:
        num = len(MODELS.WishList.objects.filter(item_category=4, item_id=comment.id))
        print ("bbbbbbb")
        return num
    except:
        return 0

def beer_is_wished(user, beer):
    try:
        return MODELS.WishList.objects.get(item_category=1, item_id=beer.id, user_id=user.id)
    except:
        return False

def deleteBeerWish(user, beer):
    try:
        wish = MODELS.WishList.objects.get(item_category=1, item_id=beer.id, user_id=user.id)
        wish.delete()
        return True
    except:
        return False

def addBeerWish(user, beer):
    try:
        wish = MODELS.WishList()
        wish.item_category = 1
        wish.item_id = beer.id
        wish.user = user
        wish.save()
        return True
    except:
        return False
