# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
import common.models as MODELS
import user.services as SERVICES
import user.forms as FORMS
import logging

logger = logging.getLogger('app')

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


def updateUser(request):
    #更新処理を入れる
    form = FORMS.updateUserForm(request.POST)
    if form.is_valid():
        user = SERVICES.selectUserById(request.user.id)
        user.gender_style = form.cleaned_data.get('gender_style')
        user.living_country = form.cleaned_data.get('living_country')
        user.living_area = form.cleaned_data.get('living_area')
        user.description = form.cleaned_data.get('description')
        user = SERVICES.updateUser(user)

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

    if key is None:
        friend = MODELS.CustomUser()
        friend.id = 0
        friend.username = '存在しません'
    else:
        friend = SERVICES.selectUserById(key)
        comment_list = SERVICES.selectCommentListByUser(friend)

    c.update({'friend':friend})
    c.update({'comment_list':comment_list})

    return show(request, c)

def show(request, c):

    #フォロー判断
    friend = c['friend']
    following = SERVICES.isFollowing(request.user, friend)
    c.update({'following':following})

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
