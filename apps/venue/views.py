# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
import venue.services as SERVICES
import logging

logger = logging.getLogger('app')

def venueDetail(request):
    logger.info('venue')
    c = {}

    if request.method == "POST":
        key = request.POST["key"]

    if key is None:
        return HOME_VIEWS.index(request)
    else:
        return venueDetailInfo(request, key)

def venueDetailInfo(request, key):
    c = {}
    venue = SERVICES.selectVenueById(key)
    comment_list = SERVICES.selectCommentListByVenue(venue)
    beer_list = SERVICES.selectBeerListByVenue(venue)
    brewery_list = SERVICES.selectBreweryListByBeerList(beer_list)

    c.update({'venue':venue})
    c.update({'comment_list':comment_list})
    c.update({'beer_list':beer_list})
    c.update({'brewery_list':brewery_list})
    return showVenueDetail(request, c)

def showVenueDetail(request, c):
    main_url = CONFIG.TOP_URL
    page_title = CONFIG.VENUE_PAGE_TITLE_URL
    main_content = CONFIG.VENUE_MAIN_URL
    sub_content = CONFIG.VENUE_SUB_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                }
    c.update({'html_title':CONFIG.VENUE_HTML_TITLE})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)
