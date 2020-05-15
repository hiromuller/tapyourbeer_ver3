# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db.models import Q
from django.db import transaction
from decimal import Decimal
from core import settings as SETTING
import logging
import random

#最大SQL発行数
MAX_SEARCH = 401
#誤差範囲
DIFF_POINT = 4/(MAX_SEARCH+1)


logger = logging.getLogger('app')

def validateDetailSearchFormCondition(detail_search_form):
    if detail_search_form.is_valid():
        overall = detail_search_form.cleaned_data['overall']
        bitterness = detail_search_form.cleaned_data['bitterness']
        aroma = detail_search_form.cleaned_data['aroma']
        drinkability = detail_search_form.cleaned_data['drinkability']
        body = detail_search_form.cleaned_data['body']
        pressure = detail_search_form.cleaned_data['pressure']
        specialness = detail_search_form.cleaned_data['specialness']
        if overall == bitterness == aroma == drinkability == body == pressure == specialness == 0:
            return False
        else:
            return True

    return False

def selectDetailSearchResultList(keys):
    """
    味わい検索で入力されたキーワードからビールを検索する。
    引数：keys味わい指標（overall, bitterness, aroma, body, drinkability, pressure, specialness)
    返り値：Beerリスト（list[Beer1, Beer2....]）
    """
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
        absolute_value = Decimal(4/(MAX_SEARCH - 1) * i).quantize(Decimal("0.01"))

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

        result_list = MODELS.BeerTasteAvg.objects.filter(condition_overall & condition_bitterness & condition_aroma & condition_body & condition_drinkability & condition_pressure & condition_specialness)

        beer_taste_avg_list.extend(result_list)
        beer_taste_avg_list = sorted(set(beer_taste_avg_list), key=beer_taste_avg_list.index)

        if len(beer_taste_avg_list) >= 100:
            break

    beer_list = []
    for beer_taste_avg in beer_taste_avg_list:
        beer_list.append(beer_taste_avg.beer)

    return beer_list
