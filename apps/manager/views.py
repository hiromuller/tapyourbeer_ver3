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
import user.views as USER_VIEWS
import brewery.views as BREWERY_VIEWS
import venue.views as VENUE_VIEWS
import logging

logger = logging.getLogger('app')

def deleteComment(request):
    if request.method == "POST":
        key = request.POST.get("key")

    if key:
        user = SERVICES.selectUserByCommentId(key)
        SERVICES.deleteCommentById(key)
        comment_list = SERVICES.selectCommentListByUser(user)

    #ユーザ画面に遷移する処理を入れる
    c = {}
    c.update({'friend':user})
    c.update({'comment_list':comment_list})
    return USER_VIEWS.show(request, c)


def mergeBrewery(request):
    form = FORMS.mergeBreweryForm(request.POST)

    if form.is_valid():
        """
        brewery(U), beer(U), TCBFParticipant(U), brewerymanager(U)
        1. brewerymanagerテーブルから、merging_brewery_idのレコードをbase_brewery_idにupdateする。すでにレコードが存在した場合はmerging_brewery_idのレコードを削除する。
        2. TCBFParticipantテーブルから、merging_brewery_idのレコードをbase_brewery_idにupdateする。すでにレコードが存在した場合はmerging_brewery_idのレコードを削除する。
        3. beerテーブルから、merging_brewery_idのレコードをbase_brewery_idにupdateする。
        4. breweryテーブルからmerging_breweryを削除する
        """
        base_brewery = SERVICES.selectBreweryById(form.cleaned_data.get('base_brewery_id'))
        merging_brewery = SERVICES.selectBreweryById(form.cleaned_data.get('merging_brewery_id'))

        SERVICES.updateBreweryManagerBreweryMerge(base_brewery, merging_brewery)
        SERVICES.updateTCBFParticipantBreweryMerge(base_brewery, merging_brewery)
        SERVICES.updateBeerBreweryMerge(base_brewery, merging_brewery)
        SERVICES.deleteBreweryByBrewery(merging_brewery)
    else:
        return SEARCH_VIEWS.index(request)

    return BREWERY_VIEWS.breweryDetailInfo(request, base_brewery.id)


def showBreweryMerge(request):
    logger.info('show breweru merge form')
    c = {}
    if request.method == "POST":
        key = request.POST.get("key")

    if key:
        form = FORMS.mergeBreweryForm(initial = {'base_brewery_id':key})
    else:
        form = FORMS.mergeBreweryForm()

    c.update({'merge_brewery_form':form})

    return show(request, c)


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

def updateVenue(request):
    form = FORMS.updateVenueForm(request.POST)
    if request.method == "POST":
        venue_id = request.POST.get("venue_id")

    if form.is_valid() and venue_id:
        venue = SERVICES.selectVenueById(venue_id)
        venue.name = COMMON_SERVICES.normalizeStr(form.cleaned_data.get('name'))
        try:
            venue.address = COMMON_SERVICES.normalizeStr(form.cleaned_data.get('address'))
        except:
            venue.address = None
        try:
            venue.description = COMMON_SERVICES.normalizeStr(form.cleaned_data.get('description'))
        except:
            venue.description = None
        venue.save()
    else:
        return SEARCH_VIEWS.index(request)

    c = {}
    comment_list = SERVICES.selectCommentListByVenue(venue)
    c.update({'venue':venue})
    c.update({'comment_list':comment_list})
    return VENUE_VIEWS.showVenueDetail(request, c)


def showVenueUpdate(request):
    logger.info('show venue update form')
    c = {}
    if request.method == "POST":
        key = request.POST.get("key")

    if not key:
        return SEARCH_VIEWS.index(request)

    venue = SERVICES.selectVenueById(key)
    form = FORMS.updateVenueForm(initial = {
                                        'name':venue.name,
                                        'address':venue.address,
                                        'description':venue.description,
                                        })

    c.update({'venue':venue})
    c.update({'venue_update_form':form})

    return show(request, c)


def updateBrewery(request):
    form = FORMS.updateBreweryForm(request.POST)
    if request.method == "POST":
        brewery_id = request.POST.get("brewery_id")

    if form.is_valid() and brewery_id:
        brewery = SERVICES.selectBreweryById(brewery_id)
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


    return BREWERY_VIEWS.breweryDetailInfo(request, brewery.id)


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
