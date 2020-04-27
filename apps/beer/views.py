# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
import beer.services as SERVICES
import home.views as HOME_VIEWS
import logging

logger = logging.getLogger('app')

def showAddBeerForm(request):
    logger.info('add beer form')
    c = {}

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.ADD_BEER_EVALUATION_PAGE_TITLE_URL
    main_content = CONFIG.ADD_BEER_EVALUATION_MAIN_URL
    sub_content = CONFIG.ADD_BEER_SUB_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                }
    c.update({'html_title':CONFIG.ADD_BEER_EVALUATION_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)


def beerDetail(request):
    logger.info('beer_detail')
    c = {}

    if request.method == "POST":
        key = request.POST["key"]

    if key is None:
        return HOME_VIEWS.index(request)

    beer = SERVICES.selectBeerById(key)
    brewery = SERVICES.selectBreweryById(beer.brewery_id)
    beer_taste_avg = SERVICES.selectBeerTasteAvgByBeer(beer)
    comment_list = SERVICES.selectCommentListByBeer(beer)
    venue_list = SERVICES.selectVenueListByBeer(beer)

    c.update({'beer':beer})
    c.update({'brewery':brewery})
    c.update({'beer_taste_avg':beer_taste_avg})
    c.update({'comment_list':comment_list})
    c.update({'venue_list':venue_list})
    return showBeerDetail(request, c)


def showBeerDetail(request, c):

    main_url = CONFIG.TOP_URL
    page_title = CONFIG.BEER_PAGE_TITLE_URL
    main_content = CONFIG.BEER_MAIN_URL
    sub_content = CONFIG.BEER_SUB_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                }
    c.update({'html_title':CONFIG.BEER_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)
