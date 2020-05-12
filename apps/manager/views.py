# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
import manager.services as SERVICES
import manager.forms as FORMS
import common.services as COMMON_SERVICES
import search.views as SEARCH_VIEWS
import beer.views as BEER_VIEWS
import brewery.views as BREWERY_VIEWS
import logging

logger = logging.getLogger('app')

def deleteComment(request):
    if request.method == "POST":
        key = request.POST.get("key")

    if key:
        SERVICES.deleteCommentById(key)

    return SEARCH_VIEWS.index(request)


def mergeBeer(request):
    form = FORMS.mergeBeerForm(request.POST)

    if form.is_valid():
        """
        #beer(U), todaystap(U), comment(U), beertasteavg(U)
        1. beertasteavgテーブルからmerging_beerを削除
        2. commentテーブルから、merging_beer_idのコメントをbase_beer_idにupdateする
        3. todaystapテーブルから、merging_beer_idのレコードをbase_beer_idにupdateする
        4. beerテーブルからmerging_beerを削除
        """
        base_beer = SERVICES.selectBeerById(form.cleaned_data.get('base_beer_id'))
        merging_beer = SERVICES.selectBeerById(form.cleaned_data.get('merging_beer_id'))

        SERVICES.deleteBeerTasteAvgByBeer(merging_beer)
        SERVICES.updateCommentBeerMerge(base_beer, merging_beer)
        SERVICES.updateTodaystapBeerMerge(base_beer, merging_beer)
        SERVICES.deleteBeerByBeer(merging_beer)
    else:
        return SEARCH_VIEWS.index(request)

    return BEER_VIEWS.beerDetailInfo(request, base_beer.id)


def showBeerMerge(request):
    logger.info('show beer merge form')
    c = {}
    if request.method == "POST":
        key = request.POST.get("key")

    if key:
        form = FORMS.mergeBeerForm(initial = {'base_beer_id':key})
    else:
        form = FORMS.mergeBeerForm()

    c.update({'merge_beer_form':form})

    return show(request, c)


def updateBrewery(request):
    form = FORMS.updateBreweryForm(request.POST)
    if request.method == "POST":
        brewery_id = request.POST.get("brewery_id")

    if form.is_valid() and brewery_id:
        brewery = SERVICES.selectBreweryById(beer_id)
        brewery.name = COMMON_SERVICES.normalizeStr(form.cleaned_data.get('name'))
        try:
            brewery.address = COMMON_SERVICES.normalizeStr(form.cleaned_data.get('address'))
        except:
            brewery.address = None
        try:
            brewery.description = COMMON_SERVICES.normalizeStr(form.cleaned_data.get('description'))
        except:
            brewery.description = None
        brewery.save()
    else:
        return SEARCH_VIEWS.index(request)

    return SEARCH_VIEWS.index(request)
    #brewery viewができたら以下に修正
    #return BREWERY_VIEWS.breweryDetailInfo(request, brewery.id)


def showBreweryUpdate(request):
    logger.info('show brewery update form')
    c = {}
    if request.method == "POST":
        key = request.POST.get("key")

    if not key:
        return SEARCH_VIEWS.index(request)

    brewery = SERVICES.selectBreweryById(key)
    form = FORMS.updateBreweryForm(initial = {
                                        'name':brewery.name,
                                        'address':brewery.address,
                                        'description':brewery.description,
                                        })

    c.update({'brewery':brewery})
    c.update({'brewery_update_form':form})

    return show(request, c)


def updateBeer(request):
    form = FORMS.updateBeerForm(request.POST)
    if request.method == "POST":
        beer_id = request.POST.get("beer_id")

    if form.is_valid() and beer_id:
        beer = SERVICES.selectBeerById(beer_id)
        beer.name = COMMON_SERVICES.normalizeStr(form.cleaned_data.get('name'))
        try:
            beer.style = COMMON_SERVICES.normalizeStr(form.cleaned_data.get('style'))
        except:
            beer.style = None
        try:
            beer.description = COMMON_SERVICES.normalizeStr(form.cleaned_data.get('description'))
        except:
            beer.description = None
        try:
            beer.ibu = COMMON_SERVICES.normalizeStr(form.cleaned_data.get('ibu'))
        except:
            beer.ibu = None
        try:
            beer.abv = COMMON_SERVICES.normalizeStr(form.cleaned_data.get('abv'))
        except:
            beer.abv = None
        beer.save()
    else:
        return SEARCH_VIEWS.index(request)

    return BEER_VIEWS.beerDetailInfo(request, beer.id)

def showBeerUpdate(request):
    logger.info('show beer update form')
    c = {}
    if request.method == "POST":
        key = request.POST.get("key")

    if not key:
        return SEARCH_VIEWS.index(request)

    beer = SERVICES.selectBeerById(key)
    form = FORMS.updateBeerForm(initial = {
                                        'name':beer.name,
                                        'style':beer.style,
                                        'description':beer.description,
                                        'ibu':beer.ibu,
                                        'abv':beer.abv,
                                        })

    c.update({'beer':beer})
    c.update({'beer_update_form':form})

    return show(request, c)

def index(request):
    logger.info('beer')
    c = {}
    return show(request, c)

def show(request, c):
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
