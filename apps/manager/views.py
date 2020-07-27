# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, redirect
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

def latestComment(request):
    c = {}
    comment_list = SERVICES.selectLatestCommentList()
    c.update({'latest_comment_list':comment_list})
    return show(request, c)

def latestUsers(request):
    c = {}
    user_list = SERVICES.selectLatestUserList()
    c.update({'latest_user_list':user_list})
    return show(request, c)

def untouchedBrewery(request):
    c = {}
    untouched_brewery_list = SERVICES.selectUntouchedBrewery()
    c.update({'untouched_brewery_list':untouched_brewery_list})

    return show(request, c)

def untouchedBeer(request):
    c = {}
    untouched_beer_list = SERVICES.selectUntouchedBeer()
    c.update({'untouched_beer_list':untouched_beer_list})

    return show(request, c)

def untouchedVenue(request):
    c = {}
    untouched_venue_list = SERVICES.selectUntouchedVenue()
    c.update({'untouched_venue_list':untouched_venue_list})

    return show(request, c)

def deleteComment(request):
    if request.method == "POST":
        key = request.POST.get("key")

    if key:
        user = SERVICES.selectUserByCommentId(key)
        SERVICES.deleteCommentById(key)
        comment_list = SERVICES.selectCommentListByUser(user)

    return redirect('/user/?user='+str(user.id))


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

    #return BREWERY_VIEWS.breweryDetailInfo(request, base_brewery.id)
    return redirect('/brewery/?brewery='+str(base_brewery.id))

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

    #return BEER_VIEWS.beerDetailInfo(request, base_beer.id)
    return redirect('/beer/?beer='+str(base_beer.id))

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

def showVenueMerge(request):
    logger.info('show venue merge form')
    c = {}
    if request.method == "POST":
        key = request.POST.get("key")

    if key:
        form = FORMS.mergeVenueForm(initial = {'base_venue_id':key})
    else:
        form = FORMS.mergeVenueForm()

    c.update({'merge_venue_form':form})

    return show(request, c)

def mergeVenue(request):
    form = FORMS.mergeVenueForm(request.POST)

    if form.is_valid():
        """
        #venue(U), todaystap(U), comment(U), venuemanager(U)
        1. todaystapテーブルからmerging_venue_idのレコードをbase_venue_idにupdateする
        2. commentテーブルから、merging_venue_idのコメントをbase_venue_idにupdateする
        3. venuemanagerテーブルから、merging_venue_idのレコードをbase_venue_idにupdateする
        4. venueテーブルからmerging_venueを削除
        """
        base_venue = SERVICES.selectVenueById(form.cleaned_data.get('base_venue_id'))
        merging_venue = SERVICES.selectVenueById(form.cleaned_data.get('merging_venue_id'))

        SERVICES.updateTodaystapVenueMerge(base_venue, merging_venue)
        SERVICES.updateCommentVenueMerge(base_venue, merging_venue)
        SERVICES.updateVenuemanagerVenueMerge(base_venue, merging_venue)
        SERVICES.deleteVenueByVenue(merging_venue)
    else:
        return SEARCH_VIEWS.index(request)

    #return VENUE_VIEWS.venueDetailInfo(request, base_venue.id)
    return redirect('/venue/?venue='+str(base_venue.id))

def updateVenue(request):
    form = FORMS.updateVenueForm(request.POST)
    if request.method == "POST":
        venue_id = request.POST.get("venue_id")

    venue = SERVICES.selectVenueById(venue_id)
    previous_photo = venue.photo

    if venue:
        form = FORMS.updateVenueForm(request.POST, request.FILES, instance=venue)
    else:
        return SEARCH_VIEWS.index(request)

    if form.is_valid():
        """
        venue = SERVICES.selectVenueById(venue_id)
        venue.name = COMMON_SERVICES.normalizeStr(form.cleaned_data.get('name'))
        try:
            venue.address = form.cleaned_data.get('address')
        except:
            venue.address = None
        try:
            venue.description = form.cleaned_data.get('description')
        except:
            venue.description = None
        venue.save()
        """
        form.save()
        if venue.photo:
            COMMON_SERVICES.resizeImage_venue_header(venue.photo)
        if previous_photo:
            if previous_photo != str(venue.photo):
                os.remove(SETTING.MEDIA_ROOT + '/' + str(previous_photo))
                pass
    else:
        return SEARCH_VIEWS.index(request)

    #return VENUE_VIEWS.venueDetailInfo(request, venue.id)
    return redirect('/venue/?venue='+str(venue.id))


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
                                        'photo':venue.photo,
                                        })

    c.update({'venue':venue})
    c.update({'venue_update_form':form})

    return show(request, c)


def updateBrewery(request):

    if request.method == "POST":
        brewery_id = request.POST.get("brewery_id")

    brewery = SERVICES.selectBreweryById(brewery_id)
    previous_logo = brewery.logo

    if brewery:
        form = FORMS.updateBreweryForm(request.POST, request.FILES, instance=brewery)
    else:
        return SEARCH_VIEWS.index(request)

    if form.is_valid():
        """
        brewery = SERVICES.selectBreweryById(brewery_id)
        brewery.name = COMMON_SERVICES.normalizeStr(form.cleaned_data.get('name'))
        try:
            brewery.address = form.cleaned_data.get('address')
        except:
            brewery.address = None
        try:
            brewery.description = form.cleaned_data.get('description')
        except:
            brewery.description = None
        try:
            brewery.web = form.cleaned_data.get('web')
        except:
            brewery.web = None
        try:
            brewery.webshop = form.cleaned_data.get('webshop')
        except:
            brewery.webshop = None
        """
        form.save()
        if brewery.logo:
            COMMON_SERVICES.resizeImage(brewery.logo)
        if previous_logo:
            if previous_logo != str(brewery.logo):
                os.remove(SETTING.MEDIA_ROOT + '/' + str(previous_logo))
                pass
    else:
        return SEARCH_VIEWS.index(request)


    #return BREWERY_VIEWS.breweryDetailInfo(request, brewery.id)
    return redirect('/brewery/?brewery='+str(brewery.id))


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
                                        'web':brewery.web,
                                        'webshop':brewery.webshop,
                                        'logo':brewery.logo,
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
            beer.description = form.cleaned_data.get('description')
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

    #return BEER_VIEWS.beerDetailInfo(request, beer.id)
    return redirect('/beer/?beer='+str(beer.id))

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
