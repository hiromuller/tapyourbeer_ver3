# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
import common.models as MODELS
import common.services as COMMON_SERVICES
import beer.services as BEER_SERVICES
import user.services as SERVICES
import user.forms as FORMS
import logging

logger = logging.getLogger('app')

def followerInfo(request):
    logger.info('follower info')
    c = {}
    if request.method == "POST":
        key = request.POST.get("key")

    user = SERVICES.selectUserById(key)
    follower_list = SERVICES.selectFollowerListByUser(user)
    num_follower = SERVICES.getNumFollower(user)

    c.update({'follower_list':follower_list})
    c.update({'num_follower':num_follower})
    return showFollowInfo(request, c)

def followInfo(request):
    logger.info('follow info')
    c = {}
    if request.method == "POST":
        key = request.POST.get("key")

    user = SERVICES.selectUserById(key)
    follow_list = SERVICES.selectFollowListByUser(user)
    num_follow = SERVICES.getNumFollow(user)

    c.update({'follow_list':follow_list})
    c.update({'num_follow':num_follow})
    return showFollowInfo(request, c)

def showFollowInfo(request, c):
    main_url = CONFIG.TOP_URL
    page_title = CONFIG.USER_PAGE_TITLE_URL
    main_content = CONFIG.USER_FOLLOW_INFO_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                }
    c.update({'html_title':CONFIG.USER_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)

def follow(request):
    logger.info('follow')
    c = {}
    if request.method == "POST":
        key = request.POST.get("key")

    if key:
        friend = SERVICES.selectUserById(key)
        follow = SERVICES.followFriend(request.user, friend)

    comment_list = SERVICES.selectCommentListByUser(friend)
    c.update({'friend':friend})
    c.update({'comment_list':comment_list})

    return show(request, c)


def unfollow(request):
    logger.info('unfollow')
    c = {}
    if request.method == "POST":
        key = request.POST.get("key")

    if key:
        friend = SERVICES.selectUserById(key)
        SERVICES.unfollowFriend(request.user, friend)

    comment_list = SERVICES.selectCommentListByUser(friend)
    c.update({'friend':friend})
    c.update({'comment_list':comment_list})

    return show(request, c)

def userBeerDetail(request):
    logger.info('user')
    c = {}

    if request.method == "POST":
        key = request.POST["key"]
    return redirect('/user-beer/?comment='+key)

def userBeerDetailGet(request):
    if request.method == "GET":
        comment_id = request.GET.get("comment")

    c ={}
    comment = SERVICES.selectCommentById(comment_id)

    beer_taste_avg = BEER_SERVICES.selectBeerTasteAvgByBeer(comment.beer)
    comment_list = SERVICES.selectCommentListByBeerExcludeTargetComment(comment.beer, comment)

    keys = {'overall':beer_taste_avg.overall,
            'bitterness':beer_taste_avg.bitterness,
            'aroma':beer_taste_avg.aroma,
            'body':beer_taste_avg.body,
            'drinkability':beer_taste_avg.drinkability,
            'pressure':beer_taste_avg.pressure,
            'specialness':beer_taste_avg.specialness,
            }
    result_beer_list = SERVICES.selectSimilarBeer(keys)
    similar_beer_list = []
    for result_beer in result_beer_list:
        if not result_beer.id == comment.beer.id:
            result_beer.photo = SERVICES.selectRandomBeerPhotoByBeer(result_beer)
            similar_beer_list.append(result_beer)

    reply_form = FORMS.replyForm()

    reply_list = SERVICES.selectReplyListByComment(comment)

    page = request.GET.get('page', 1)
    paginator = Paginator(comment_list, 5)

    try:
        paginate_comment_list = paginator.page(page)
    except PageNotAnInteger:
        paginate_comment_list = paginator.page(1)
    except EmptyPage:
        paginate_comment_list = paginator.page(paginator.num_pages)


    c.update({'user_comment':comment})
    c.update({'beer':comment.beer})
    c.update({'brewery':comment.beer.brewery})
    c.update({'beer_taste_avg':beer_taste_avg})
    c.update({'comment_list':paginate_comment_list})
    c.update({'similar_beer_list':similar_beer_list})
    c.update({'reply_list':reply_list})
    c.update({'reply_form':reply_form})


    main_url = CONFIG.TOP_URL
    page_title = CONFIG.USER_BEER_DETAIL_PAGE_TITLE_URL
    main_content = CONFIG.USER_BEER_DETAIL_MAIN_URL
    sub_content = CONFIG.USER_BEER_DETAIL_SUB_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                }
    c.update({'html_title':CONFIG.USER_BEER_DETAIL_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)


def updateUser(request):
    #更新処理を入れる
    user = request.user
    previous_photo = request.user.photo
    form = FORMS.updateUserForm(request.POST, request.FILES, instance=user)
    if form.is_valid():
        form.save()
        if user.photo:
            COMMON_SERVICES.resizeProfileImage(user.photo)
        if previous_photo:
            if previous_photo != str(user.photo):
                os.remove(SETTING.MEDIA_ROOT + '/' + str(previous_photo))
                pass

    c ={}
    comment_list = SERVICES.selectCommentListByUser(user)
    c.update({'friend':user})
    c.update({'comment_list':comment_list})

    return show(request, c)

def showUserUpdate(request):
    logger.info('show user update form')
    c = {}
    if request.method == "POST":
        key = request.POST.get("key")

    if not key:
        return showUser(request)

    user = request.user
    form = FORMS.updateUserForm(initial = {
                                        'gender_style':user.gender_style,
                                        'living_area':user.living_area,
                                        'living_country':user.living_country,
                                        'description':user.description,
                                        'photo':user.photo,
                                        })
    c.update({'update_user_form':form})

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.USER_PAGE_TITLE_URL
    main_content = CONFIG.USER_UPDATE_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                }
    c.update({'html_title':CONFIG.USER_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)


def showUser(request):
    logger.info('user')
    c = {}

    if request.method == "POST":
        key = request.POST["key"]
    return redirect('/user/?user='+key)


def showUserGet(request):
    logger.info('user')
    c = {}

    if request.method == "GET":
        try:
            key = request.GET["user"]
        except:
            key = None
        try:
            wishlist_flg = request.GET["wishlist"]
        except:
            wishlist_flg = False


    if key is None:
        friend = MODELS.CustomUser()
        friend.id = 0
        friend.username = '存在しません'
        comment_list = []
    else:
        friend = SERVICES.selectUserById(key)
        comment_list = SERVICES.selectCommentListByUser(friend)

    c.update({'comment_list':comment_list})
    c.update({'friend':friend})

    if wishlist_flg:
        return showWishList(request, c)

    return show(request, c)

def showWishList(request, c):
    c.update({'num_drink':len(c['comment_list'])})

    wish_list = SERVICES.selectWishListByUser(c['friend'])

    page = request.GET.get('page', 1)
    paginator = Paginator(wish_list, 5)

    try:
        paginate_wish_list = paginator.page(page)
    except PageNotAnInteger:
        paginate_wish_list = paginator.page(1)
    except EmptyPage:
        paginate_wish_list = paginator.page(paginator.num_pages)
    c.update({'wish_list':paginate_wish_list})

    return showPage(request, c)

def show(request, c):

    c.update({'num_drink':len(c['comment_list'])})

    page = request.GET.get('page', 1)
    paginator = Paginator(c['comment_list'], 6)

    try:
        paginate_comment_list = paginator.page(page)
    except PageNotAnInteger:
        paginate_comment_list = paginator.page(1)
    except EmptyPage:
        paginate_comment_list = paginator.page(paginator.num_pages)
    c.update({'comment_list':paginate_comment_list})

    return showPage(request, c)

def showPage(request, c):

    #フォロー判断
    friend = c['friend']
    following = SERVICES.isFollowing(request.user, friend)
    num_follower = SERVICES.getNumFollower(friend)
    num_follow = SERVICES.getNumFollow(friend)
    c.update({'following':following})
    c.update({'num_follower':num_follower})
    c.update({'num_follow':num_follow})

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.USER_PAGE_TITLE_URL
    main_content = CONFIG.USER_MAIN_URL
    sub_content = CONFIG.USER_SUB_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                }
    c.update({'html_title':CONFIG.USER_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)
