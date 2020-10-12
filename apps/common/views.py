# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from django.http.response import JsonResponse
from core import consts as CONST
from core import configs as CONFIG
from core import settings as SETTING
import common.services as SERVICES
import common.models as MODELS
import home.views as HOME_VIEWS
import beer.views as BEER_VIEWS
import brewery.views as BREWERY_VIEWS
import manager.views as MANAGER_VIEWS
import search.views as SEARCH_VIEWS
import detail_search.views as DETAIL_SEARCH_VIEWS
import news.views as NEWS_VIEWS
import user.views as USER_VIEWS
import venue.views as VENUE_VIEWS
import accounts.views as ACCOUNTS_VIEWS
import logging
logger = logging.getLogger('app')

def index(request):
    if request.method =="POST":
        action = request.POST["action"]
    else:
        action = CONFIG.ACTION_HOME

    print (action)

    if action == CONFIG.ACTION_HOME:
        return HOME_VIEWS.Home(request)
    elif action == CONFIG.ACTION_SIGNUP:
        return ACCOUNTS_VIEWS.signup_index(request)
    elif action == CONFIG.ACTION_SIGNUP_USER:
        return ACCOUNTS_VIEWS.signup_user(request)
    elif action == CONFIG.ACTION_BEER_DETAIL:
        return BEER_VIEWS.beerDetail(request)
    elif action == CONFIG.ACTION_ADD_BEER_EVALUATION_FORM:
        return BEER_VIEWS.addBeerEvaluationForm(request)
    elif action == CONFIG.ACTION_ADD_BEER_EVALUATION:
        return BEER_VIEWS.addBeerEvaluation(request)
    elif action == CONFIG.ACTION_BREWERY_DETAIL:
        return BREWERY_VIEWS.breweryDetail(request)
    elif action == CONFIG.ACTION_MANAGER_ACCOUNT:
        return MANAGER_VIEWS.index(request)
    elif action == CONFIG.ACTION_SEARCH:
        return SEARCH_VIEWS.index(request)
    elif action == CONFIG.ACTION_SEARCH_LIST:
        return SEARCH_VIEWS.searchList(request)
    elif action == CONFIG.ACTION_DETAIL_SEARCH:
        return DETAIL_SEARCH_VIEWS.index(request)
    elif action == CONFIG.ACTION_DETAIL_SEARCH_LIST:
        return DETAIL_SEARCH_VIEWS.detailSearchList(request)
    elif action == CONFIG.ACTION_NEWS:
        return NEWS_VIEWS.news(request)
    elif action == CONFIG.ACTION_USER_ACCOUNT:
        return USER_VIEWS.showUser(request)
    elif action == CONFIG.ACTION_USER_UPDATE:
        return USER_VIEWS.showUserUpdate(request)
    elif action == CONFIG.ACTION_UPDATE_USER:
        return USER_VIEWS.updateUser(request)
    elif action == CONFIG.ACTION_FOLLOW:
        return USER_VIEWS.follow(request)
    elif action == CONFIG.ACTION_UNFOLLOW:
        return USER_VIEWS.unfollow(request)
    elif action == CONFIG.ACTION_FOLLOW_INFO:
        return USER_VIEWS.followInfo(request)
    elif action == CONFIG.ACTION_FOLLOWER_INFO:
        return USER_VIEWS.followerInfo(request)
    elif action == CONFIG.ACTION_USER_BEER_DETAIL:
        return USER_VIEWS.userBeerDetail(request)
    elif action == CONFIG.ACTION_VENUE_DETAIL:
        return VENUE_VIEWS.venueDetail(request)
    elif action == CONFIG.ACTION_DELETE_COMMENT:
        return MANAGER_VIEWS.deleteComment(request)
    elif action == CONFIG.ACTION_BEER_UPDATE:
        return MANAGER_VIEWS.showBeerUpdate(request)
    elif action == CONFIG.ACTION_UPDATE_BEER:
        return MANAGER_VIEWS.updateBeer(request)
    elif action == CONFIG.ACTION_BREWERY_UPDATE:
        return MANAGER_VIEWS.showBreweryUpdate(request)
    elif action == CONFIG.ACTION_UPDATE_BREWERY:
        return MANAGER_VIEWS.updateBrewery(request)
    elif action == CONFIG.ACTION_BEER_MERGE:
        return MANAGER_VIEWS.showBeerMerge(request)
    elif action == CONFIG.ACTION_MERGE_BEER:
        return MANAGER_VIEWS.mergeBeer(request)
    elif action == CONFIG.ACTION_BREWERY_MERGE:
        return MANAGER_VIEWS.showBreweryMerge(request)
    elif action == CONFIG.ACTION_MERGE_BREWERY:
        return MANAGER_VIEWS.mergeBrewery(request)
    elif action == CONFIG.ACTION_VENUE_UPDATE:
        return MANAGER_VIEWS.showVenueUpdate(request)
    elif action == CONFIG.ACTION_UPDATE_VENUE:
        return MANAGER_VIEWS.updateVenue(request)
    elif action == CONFIG.ACTION_VENUE_MERGE:
        return MANAGER_VIEWS.showVenueMerge(request)
    elif action == CONFIG.ACTION_MERGE_VENUE:
        return MANAGER_VIEWS.mergeVenue(request)
    elif action == CONFIG.ACTION_UNTOUCHED_BREWERY:
        return MANAGER_VIEWS.untouchedBrewery(request)
    elif action == CONFIG.ACTION_UNTOUCHED_BEER:
        return MANAGER_VIEWS.untouchedBeer(request)
    elif action == CONFIG.ACTION_UNTOUCHED_VENUE:
        return MANAGER_VIEWS.untouchedVenue(request)
    elif action == CONFIG.ACTION_LATEST_COMMENT:
        return MANAGER_VIEWS.latestComment(request)
    elif action == CONFIG.ACTION_LATEST_USERS:
        return MANAGER_VIEWS.latestUsers(request)
    else:
        return view(request)

def view(request):
    return HOME_VIEWS.Home(request)

def like(request, comment_id):
    logger.info('like method')
    comment = SERVICES.selectCommentById(comment_id)
    if comment:
        if SERVICES.is_liked(request.user, comment):
            result = SERVICES.deleteLike(request.user, comment)
            like_img = '/static/images/pre_like.png'
        else:
            result = SERVICES.addLike(request.user, comment)
            like_img = '/static/images/liked.png'
        num_like = SERVICES.getLikeCount(comment)
    else:
        num_like = 0

    return JsonResponse({"like":num_like, "like_img":like_img})


def comment_wish(request, item_id):
    logger.info('comment wish method')
    comment = SERVICES.selectCommentById(item_id)
    if comment:
        if SERVICES.comment_is_wished(request.user, comment):
            result = SERVICES.deleteCommentWish(request.user, comment)
            wish_img = '/static/images/wishlist_off.png'
        else:
            result = SERVICES.addCommentWish(request.user, comment)
            wish_img = '/static/images/wishlist_on.png'
        num_wish = SERVICES.getCommentWishCount(comment)
    else:
        num_wish = 0

    return JsonResponse({"wish":num_wish, "wish_img":wish_img})


def beer_wish(request, item_id):
    logger.info('beer wish method')
    beer = SERVICES.selectBeerById(item_id)
    if beer:
        if SERVICES.beer_is_wished(request.user, beer):
            result = SERVICES.deleteBeerWish(request.user, beer)
            wished = False
        else:
            result = SERVICES.addBeerWish(request.user, beer)
            wished = True

    return JsonResponse({"wished":wished})

def brewery_wish(request, item_id):
    logger.info('brewery wish method')
    brewery = SERVICES.selectBreweryById(item_id)
    if brewery:
        if SERVICES.brewery_is_wished(request.user, brewery):
            result = SERVICES.deleteBreweryWish(request.user, brewery)
            wished = False
        else:
            result = SERVICES.addBreweryWish(request.user, brewery)
            wished = True

    return JsonResponse({"wished":wished})

def venue_wish(request, item_id):
    logger.info('venue wish method')
    venue = SERVICES.selectVenueById(item_id)
    if venue:
        if SERVICES.venue_is_wished(request.user, venue):
            result = SERVICES.deleteVenueWish(request.user, venue)
            wished = False
        else:
            result = SERVICES.addVenueWish(request.user, venue)
            wished = True

    return JsonResponse({"wished":wished})

def reply(request):
    logger.info('reply')
    input_text = request.POST.getlist("reply")
    comment_id = request.POST.getlist("comment_id")
    reply_result = SERVICES.addReply(request.user, input_text[0], comment_id[0])
    if reply_result:
        reply_response = {}
        reply_response.update({"reply":reply_result.reply})
        reply_response.update({"user_id":reply_result.user.id})
        reply_response.update({"user_username":reply_result.user.username})
        if reply_result.user.photo:
            reply_response.update({"user_photo":str(reply_result.user.photo)})
        else:
            reply_response.update({"user_photo":"images/no-profile-image.png"})
        reply_response.update({"reply_date":reply_result.date})
    else:
        reply_response = None
    return JsonResponse(reply_response)

def csrf_failure(request):
    return HOME_VIEWS.Home(request)
