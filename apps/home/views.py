# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

    comment_list = SERVICES.selectCommentListByFollowingUser(request.user)

    return homeShow(request, c, comment_list)

def world(request):
    logger.info('home world')
    c = {}

    comment_list = SERVICES.selectCommentList()

    return homeShow(request, c, comment_list)

def homeShow(request, c, comment_list):
    page = request.GET.get('page', 1)
    paginator = Paginator(comment_list, 5)
    try:
        paginate_comment_list = paginator.page(page)
    except PageNotAnInteger:
        paginate_comment_list = paginator.page(1)
    except EmptyPage:
        paginate_comment_list = paginator.page(paginator.num_pages)

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.HOME_PAGE_TITLE_URL
    main_content = CONFIG.HOME_MAIN_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                }

    c.update({'comment_list':paginate_comment_list})
    c.update({'html_title':CONFIG.HOME_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)
