# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
import manager.services as SERVICES
import search.views as SEARCH_VIEWS
import logging

logger = logging.getLogger('app')

def deleteComment(request):
    if request.method == "POST":
        key = request.POST.get("key")

    if key:
        SERVICES.deleteCommentById(key)

    return SEARCH_VIEWS.index(request)

def index(request):
    logger.info('beer')
    c = {}

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.MANAGER_PAGE_TITLE_URL
    main_content = CONFIG.MANAGER_MAIN_URL
    sub_content = CONFIG.MANAGER_SUB_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                }
    c.update({'html_title':CONFIG.MANAGER_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)
