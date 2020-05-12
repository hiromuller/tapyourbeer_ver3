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

def breweryDetail(request):
    logger.info('brewry_detail')
    c = {}

    if request.method == "POST":
        key = request.POST["key"]

    if key is None:
        return HOME_VIEWS.index(request)

    brewery = SERVICES.selectBreweryById(key)
    beer_list = SERVICES.selectBeerlistByBrewery(brewery)
    comment_list = SERVICES.selectCommentListByBrewery(brewery)
    venue_list = SERVICES.selectVenueListByBrewery(brewery)

    c.update({'brewery':brewery})
    c.update({'beer_list':beer_list})
    c.update({'comment_list':comment_list})
    c.update({'venue_list':venue_list})
    return showBreweryDetail(request, c)


def showBreweryDetail(request, c):

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.BREWERY_PAGE_TITLE_URL
    main_content = CONFIG.BREWERY_MAIN_URL
    sub_content = CONFIG.BREWERY_SUB_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                }
    c.update({'html_title':CONFIG.BREWERY_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)
