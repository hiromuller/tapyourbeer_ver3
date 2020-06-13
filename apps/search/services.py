# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db.models import Q
from django.db import transaction
from decimal import Decimal
from core import settings as SETTING
import logging
import random
import pprint

#最大検索結果数
MAX_RESULTS = 50

def selectBeerListByNameKey(key):
    beer_list = MODELS.Beer.objects.filter(name__icontains=key, is_active=True)[:MAX_RESULTS]
    return beer_list

def selectBreweryListByNameKey(key):
    brewery_list = MODELS.Brewery.objects.filter(name__icontains=key, is_active=True)[:MAX_RESULTS]
    return brewery_list

def selectVenueListByNameKey(key):
    venue_list = MODELS.Venue.objects.filter(name__icontains=key, is_active=True)[:MAX_RESULTS]
    return venue_list

def selectUserListByUsernameKey(key):
    user_list = MODELS.CustomUser.objects.filter(username__icontains=key, is_active=True)[:MAX_RESULTS]
    return user_list


def selectCommentListByUserOverallvalue(user):
    try:
        comment_list = []
        n = 5
        for i in range(5):
            comment_list.extend(MODELS.Comment.objects.filter(user=user, overall=n).order_by('?')[:30])
            n = n - 1
        del comment_list[30:]
        return comment_list
    except:
        return None


def calculateUserEvaluationAveragebyUserEvaluationValue(user):
    try:
        comment_list = selectCommentListByUserOverallvalue(user)
        bitterness_value_list = []
        aroma_value_list = []
        body_value_list = []
        drinkability_value_list = []
        pressure_value_list = []
        specialness_value_list = []

        for comment in comment_list:
            bitterness_value_list.append(comment.bitterness)
            aroma_value_list.append(comment.aroma)
            body_value_list.append(comment.body)
            drinkability_value_list.append(comment.drinkability)
            pressure_value_list.append(comment.pressure)
            specialness_value_list.append(comment.specialness)

        bitterness_avelage = sum(bitterness_value_list)/len(bitterness_value_list)
        aroma_avelage = sum(aroma_value_list)/len(aroma_value_list)
        body_avelage = sum(body_value_list)/len(body_value_list)
        drinkability_avelage = sum(drinkability_value_list)/len(drinkability_value_list)
        pressure_avelage = sum(pressure_value_list)/len(pressure_value_list)
        specialness_avelage = sum(specialness_value_list)/len(specialness_value_list)

        average_list = [bitterness_avelage, aroma_avelage, body_avelage, drinkability_avelage, pressure_avelage, specialness_avelage]

        return average_list

    except:
        return None


def selectRecommendedBeerbyUserEvaluationAverage(user):
    try:
        user_average_list = calculateUserEvaluationAveragebyUserEvaluationValue(user)
        beer_list = MODELS.BeerTasteAvg.objects.order_by('?')[:100]
        defference_value_list = []
        for beer in beer_list:

            beer_evaluation_elements_list = []
            beer_evaluation_elements_list.append(float(beer.bitterness))
            beer_evaluation_elements_list.append(float(beer.aroma))
            beer_evaluation_elements_list.append(float(beer.body))
            beer_evaluation_elements_list.append(float(beer.pressure))
            beer_evaluation_elements_list.append(float(beer.drinkability))
            beer_evaluation_elements_list.append(float(beer.specialness))

            evaluation_defference = []

            for a, b in zip(user_average_list, beer_evaluation_elements_list):
                evaluation_defference.append(abs(a-b))

            defference_value_list.append(sum(evaluation_defference))

        recommended_beertasteavg_index = defference_value_list.index(min(defference_value_list))
        recommended_beer_id = beer_list[recommended_beertasteavg_index].beer.id

        return MODELS.Beer.objects.get(id=recommended_beer_id)

    except:
        return None

def selectNumnerofUserComments(user):
    try:
        user_comment_list = []
        user_comment_list.extend(MODELS.Comment.objects.filter(user=user))
        return len(user_comment_list)
    except:
        return None
