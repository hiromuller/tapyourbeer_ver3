# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
import home.services as SERVICES
import logging

logger = logging.getLogger('app')

def Home(request):
    logger.info('home')
    c = {}
    if request.method == "POST":
#        key = request.POST.get("key")
        key = request.user.id

    print(request.user)
    print(request.user.id)

    customuser = SERVICES.selectCustomuserbyCustomuserID(key)
#    following_list = SERVICES.selectFollowinguserbyCustomuser(customuser)
##    follow_list = SERVICES.selectFollowuserbyFollowuserID(customuser)
#    comment_list = SERVICES.selectCommentlistbyCustomuserID(followinguser_list)
#    comment_list = SERVICES.selectCommentlistbyCustomuser(followinguser_list)
    comment_list = SERVICES.selectCommentlistbyCustomuser(customuser)

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.HOME_PAGE_TITLE_URL
    main_content = CONFIG.HOME_MAIN_URL
    sub_content = CONFIG.HOME_SUB_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                }

    c.update({'customuser':customuser})
##    c.update({'follow_list':follow_list})
    c.update({'comment_list':comment_list})

    c.update({'html_title':CONFIG.HOME_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)
