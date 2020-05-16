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

    comment_list = SERVICES.selectCommentListbyFollowingUserID(request.user)

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

    c.update({'comment_list':comment_list})

    c.update({'html_title':CONFIG.HOME_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)
