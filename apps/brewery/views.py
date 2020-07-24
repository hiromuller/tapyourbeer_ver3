# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
import brewery.services as SERVICES
import logging

logger = logging.getLogger('app')

def breweryDetail(request):
    logger.info('brewry_detail')

    if request.method == "POST":
        key = request.POST["key"]

    return redirect('/brewery/?brewery='+key)


def breweryDetailGet(request):
    logger.info('brewry_detail')

    if request.method == "GET":
        key = request.GET.get("brewery")

    if key is None:
        return HOME_VIEWS.index(request)
    return breweryDetailInfo(request, key)

def breweryDetailInfo(request, brewery_id):
    c = {}

    brewery = SERVICES.selectBreweryById(brewery_id)
    beer_list = SERVICES.selectBeerlistByBrewery(brewery)
    comment_list = SERVICES.selectCommentListByBrewery(brewery)
    venue_list = SERVICES.selectVenueListByBrewery(brewery)

    page = request.GET.get('page', 1)
    paginator = Paginator(comment_list, 5)

    try:
        paginate_comment_list = paginator.page(page)
    except PageNotAnInteger:
        paginate_comment_list = paginator.page(1)
    except EmptyPage:
        paginate_comment_list = paginator.page(paginator.num_pages)

    c.update({'brewery':brewery})
    c.update({'beer_list':beer_list})
    c.update({'comment_list':paginate_comment_list})
    c.update({'venue_list':venue_list})

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
