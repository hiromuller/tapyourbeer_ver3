# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
import search.services as SERVICES
import search.forms as FORMS
import logging

logger = logging.getLogger('app')

def searchList(request):
    logger.info('search_list')
    c = {}

    if request.method == "POST":
        form = FORMS.searchForm(request.POST)
        search_form = {'search_form':form}
        c.update(search_form)

        if form.is_valid():
            key = form.cleaned_data.get('keyword')

            #ビール取得（最大５０件）
            beer_list = SERVICES.selectBeerListByNameKey(key)
            c.update({'beer_list':beer_list})

            #ブルワリー取得（最大５０件）
            brewery_list = SERVICES.selectBreweryListByNameKey(key)
            c.update({'brewery_list':brewery_list})

            #店舗取得（最大５０件）
            venue_list = SERVICES.selectVenueListByNameKey(key)
            c.update({'venue_list':venue_list})

            #ユーザ取得（最大５０件）
            user_list = SERVICES.selectUserListByUsernameKey(key)
            c.update({'user_list':user_list})

    else:
        return index(request)


    return showSearch(request, c)

def index(request):
    logger.info('search')
    c = {}
    search_form = {'search_form':FORMS.searchForm()}
    num_user_comments = SERVICES.selectNumberofUserComments(request.user)
    if num_user_comments >= 5:
        recommended_beer = SERVICES.selectRecommendedBeerbyUserEvaluationAverage(request.user)
        c.update({'recommended_beer':recommended_beer})
    else:
        None

    c.update({'num_user_comments':num_user_comments})
    c.update(search_form)
    return showSearch(request, c)

def showSearch(request, c):
    main_url = CONFIG.TOP_URL
    page_title = CONFIG.SEARCH_PAGE_TITLE_URL
    main_content = CONFIG.SEARCH_MAIN_URL
    sub_content = CONFIG.SEARCH_SUB_URL
    search_bar = CONFIG.SEARCH_BAR_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                'search_bar':search_bar,
                }
    c.update({'html_title':CONFIG.SEARCH_HTML_TITLE})
    c.update({'move_to_detail_search_button':True})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)
