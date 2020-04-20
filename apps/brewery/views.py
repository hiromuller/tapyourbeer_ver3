# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
import brewery.services as SERVICES
import logging

logger = logging.getLogger('app')

def index(request):
    logger.info('brewery')
#    user = request.user
    c = {}

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.BREWERY_PAGE_TITLE_URL
    main_content = CONFIG.BREWERY_MAIN_URL
    sub_content = CONFIG.BREWERY_SUB_URL
    action_dict = CONFIG.ACTION_DICT
#     user_dict = {'user':user}
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                }
#    c.update({'master_user_name':SETTING.MASTER_USER_NAME})
#    c.update(csrf(request))
    c.update({'html_title':CONFIG.BREWERY_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
#     c.update(user_dict)
    return render(request, 'common/main.html', c)
#    return render(request, 'common/sample_html.html', c)
