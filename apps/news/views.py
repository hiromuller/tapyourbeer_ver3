# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
import news.services as SERVICES
import common.services as COMMON_SERVICES
import feedparser
import logging

logger = logging.getLogger('app')

def news(request):
    logger.info('news')
    c = {}


    #フィード
    entry_list = SERVICES.selectAllNewsFeedList()

    c.update({
            'entries': entry_list,
        })

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.NEWS_PAGE_TITLE_URL
    main_content = CONFIG.NEWS_MAIN_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                }

    c.update({'html_title':CONFIG.NEWS_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)
