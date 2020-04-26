# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
import detail_search.services as SERVICES
import logging

logger = logging.getLogger('app')

def index(request):
    logger.info('detail_search')
    c = {}

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.DETAIL_SEARCH_PAGE_TITLE_URL
    main_content = CONFIG.DETAIL_SEARCH_MAIN_URL
    sub_content = CONFIG.DETAIL_SEARCH_SUB_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                }
    c.update({'html_title':CONFIG.DETAIL_SEARCH_HTML_TITLE})
    c.update({'search_button':True})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)
