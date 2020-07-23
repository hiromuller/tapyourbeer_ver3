# -*- coding: utf-8 -*-
import common.models as MODELS
from django.db.models import Q
from django.db import transaction
from decimal import Decimal
from core import settings as SETTING
import logging
import random

#最大検索結果数
MAX_RESULTS = 50

def selectBeerListByNameKey(key):
    beer_list = MODELS.Beer.objects.filter(name__icontains=key, is_active=True)[:MAX_RESULTS]
    return beer_list

def selectBreweryListByNameKey(key):
    brewery_list = MODELS.Brewery.objects.filter(name__icontains=key, is_active=True)[:MAX_RESULTS]
    return brewery_list

def selectVenueListByNameKey(key):
    venue_list = MODELS.Venue.objects.filter(Q(name__icontains=key) | Q(address__icontains=key), is_active=True)[:MAX_RESULTS]
    return venue_list

def selectUserListByUsernameKey(key):
    user_list = MODELS.CustomUser.objects.filter(username__icontains=key, is_active=True)[:MAX_RESULTS]
    return user_list


def selectCommentListByUserOverallvalue(user):
    try:
        comment_list = []
        n = 5
        for i in range(5):
            comment_list.extend(MODELS.Comment.objects.filter(user=user, overall=n).order_by('?'))
            n = n - 1
            if len(comment_list)>30:
                break
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

        bitterness_average = sum(bitterness_value_list)/len(bitterness_value_list)
        aroma_average = sum(aroma_value_list)/len(aroma_value_list)
        body_average = sum(body_value_list)/len(body_value_list)
        drinkability_average = sum(drinkability_value_list)/len(drinkability_value_list)
        pressure_average = sum(pressure_value_list)/len(pressure_value_list)
        specialness_average = sum(specialness_value_list)/len(specialness_value_list)

        average_dict = {'bitterness_average':bitterness_average, 'aroma_average':aroma_average, 'body_average':body_average, 'drinkability_average':drinkability_average, 'pressure_average':pressure_average, 'specialness_average':specialness_average}

        return average_dict

    except:
        return None


def selectRecommendedBeerbyUserEvaluationAverage(user):
    try:
        user_comment_list = []
        user_comment_list.extend(MODELS.Comment.objects.filter(user=user))
        if len(user_comment_list)>=5:
            user_average_dict = calculateUserEvaluationAveragebyUserEvaluationValue(user)
            beer_list = MODELS.BeerTasteAvg.objects.order_by('?')[:100]
            defference_value_list = []
            for beer in beer_list:


                beer_evaluation_elements_dict = {}
                beer_evaluation_elements_dict['bitterness_average']=float(beer.bitterness)
                beer_evaluation_elements_dict['aroma_average']=float(beer.aroma)
                beer_evaluation_elements_dict['body_average']=float(beer.body)
                beer_evaluation_elements_dict['drinkability_average']=float(beer.drinkability)
                beer_evaluation_elements_dict['pressure_average']=float(beer.pressure)
                beer_evaluation_elements_dict['specialness_average']=float(beer.specialness)

                evaluation_defference = []

                for a, b in zip(user_average_dict.values(), beer_evaluation_elements_dict.values()):
                    evaluation_defference_value=abs(a-b)
                    evaluation_defference.append(evaluation_defference_value)

                defference_value_list.append(sum(evaluation_defference))

            recommended_beertasteavg_index = defference_value_list.index(min(defference_value_list))
        else:
            None
        return beer_list[recommended_beertasteavg_index].beer

    except:
        return None

def selectNumberofUserComments(user):
    try:
        return len(MODELS.Comment.objects.filter(user=user.id))
    except:
        return None
