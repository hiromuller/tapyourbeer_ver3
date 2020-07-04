# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
from core import messages as MSG
import beer.services as SERVICES
import beer.forms as FORMS
import common.models as MODELS
import common.services as COMMON_SERVICES
import home.views as HOME_VIEWS
import common.management.commands.createaveragetable as COMMON_COMMANDS
import logging

logger = logging.getLogger('app')

def addBeerEvaluation(request):
    logger.info('add beer evaluation')
    c = {}

    if request.method == "POST":
        form = FORMS.addCommentForm(request.POST, request.FILES)
        """
        コメント登録処理概要
        １．フォームバリデーション（エラーとなる条件はフォーム側でバリデートする）
            表示されているすべての項目が入力されている
            beer_idとbeer_nameが入力されている場合、モデルがDBと一致している
            brewery_idとbrewery_nameが入力されている場合、モデルがDBと一致している
            brewery_idとbeer_idの値があり、一致している
            brewery_idの値がなく、beer_idの値はある　→　beer_idに紐づくbreweryを取得し、入力されている名前が一致している
            venue_idが入力されている場合、venue_idとvenue_nameが一致するモデルがDBに存在している
        ２．登録処理振り分け（条件分岐エラーはこの時点ですでに存在しないが、DB接続にエラーが起こる可能性はある）
            条件１）
            brewery_id, beer_idの値がない
            　→ブルワリーテーブルをname検索で存在確認し、存在すればなにもしない、存在しなければ登録
            　→ビールテーブルをnameとブルワリーで存在確認し、存在すれば何もしない、存在しなければビールを登録する
            　→コメント登録する
            条件２）
            brewery_idの値はあるがbeer_idの値がない
            　→beer_nameとbrewery_idの同組み合わせがbeerテーブルに存在しない場合、ビールを登録し、コメントを登録する
            　→組み合わせが存在した場合、対象のbeerオブジェクトを取得し、コメントを登録する
            条件３）
            brewery_id, beer_idの値がある
            　→コメントを登録する
            brewery_idの値がなく、beer_idの値はある
            　→コメントを登録する
        """
        if form.is_valid():
            beer_id = form.cleaned_data.get('beer_id')
            beer_name = form.cleaned_data.get('beer_name')
            brewery_id = form.cleaned_data.get('brewery_id')
            brewery_name = form.cleaned_data.get('brewery_name')
            venue_id = form.cleaned_data.get('venue_id')
            venue_name = form.cleaned_data.get('venue_name')
            try:
                photo = form.cleaned_data.get('photo')
            except:
                photo = None

            #全角半角/大文字小文字加工
            brewery_name = COMMON_SERVICES.normalizeStr(brewery_name)
            beer_name = COMMON_SERVICES.normalizeStr(beer_name)
            venue_name = COMMON_SERVICES.normalizeStr(venue_name)

            all_registered = True
            if not brewery_id and not beer_id:
                if SERVICES.isBreweryExistByName(brewery_name):
                    brewery = SERVICES.selectBreweryByName(brewery_name)
                else:
                    brewery = SERVICES.addBreweryByName(brewery_name)
                if not brewery:
                    c.update({'form_message':MSG.BREWERY_NOT_ADDED})
                    all_registered = False

                if SERVICES.isBeerExistByNameAndBrewery(beer_name, brewery):
                    beer = SERVICES.selectBeerByNameAndBrewery(beer_name, brewery)
                else:
                    beer = SERVICES.addBeerByNameAndBrewery(beer_name, brewery)
                if not beer:
                    c.update({'form_message':MSG.BEER_NOT_ADDED})
                    all_registered = False

            elif brewery_id and not beer_id:
                brewery = SERVICES.selectBreweryById(brewery_id)
                beer = SERVICES.selectBeerByNameAndBrewery(beer_name, brewery)
                if not beer:
                    beer = SERVICES.addBeerByNameAndBrewery(beer_name, brewery)
                    if not beer:
                        c.update({'form_message':MSG.BEER_NOT_ADDED})
                        all_registered = False
            else:
                beer = SERVICES.selectBeerById(beer_id)

            if venue_name and not venue_id:
                if SERVICES.isVenueExistByName(venue_name):
                    venue_list = SERVICES.selectVenueListByName(venue_name)
                    venue = venue_list[0]
                else:
                    venue = SERVICES.addVenueByName(venue_name)
                if not venue:
                    c.update({'form_message':MSG.VENUE_NOT_ADDED})
                    all_registered = False
            else:
                venue = SERVICES.selectVenueById(venue_id)

            if all_registered:
                comment_dict = {
                                'beer':beer,
                                'user':request.user,
                                'venue':venue,
                                'overall':form.cleaned_data.get('overall'),
                                'bitterness':form.cleaned_data.get('bitterness'),
                                'aroma':form.cleaned_data.get('aroma'),
                                'body':form.cleaned_data.get('body'),
                                'drinkability':form.cleaned_data.get('drinkability'),
                                'pressure':form.cleaned_data.get('pressure'),
                                'specialness':form.cleaned_data.get('specialness'),
                                'comment':form.cleaned_data.get('comment'),
                                'photo':photo,
                                }
                comment = SERVICES.addCommentByDict(comment_dict)

                if comment.photo:
                    COMMON_SERVICES.resizeImage(comment.photo)

                SERVICES.deleteBeerTasteAvgByBeer(beer)
                COMMON_COMMANDS.saveAverage(beer)

                if comment:
                    return beerDetailInfo(request, beer.id)
                else:
                    c.update({'form_message':MSG.COMMENT_NOT_ADDED})

        else:
            c.update({'evaluation_missing_message':MSG.PLEASE_INSERT_ALL_EVALUATION})

        c.update({'comment_form':form})

    else:
        return addBeerEvaluationForm(request)

    return showAddBeerEvaluationForm(request, c)

def addBeerEvaluationForm(request):
    logger.info('add beer evaluation form')
    c = {}

    if request.method == "POST":
        key = request.POST.get("key")

    if key:
        beer = SERVICES.selectBeerById(key)
        form = FORMS.addCommentForm(initial = {
                                                'beer_id':beer.id,
                                                'beer_name':beer.name,
                                                'brewery_id':beer.brewery.id,
                                                'brewery_name':beer.brewery.name,
                                                })
        #form.fields['beer_name'].widget.attrs['readonly'] = 'readonly'
        #form.fields['brewery_name'].widget.attrs['readonly'] = 'readonly'
    else:
        form = FORMS.addCommentForm()

    c.update({'comment_form':form})
    return showAddBeerEvaluationForm(request, c)

def showAddBeerEvaluationForm(request, c):
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

    if request.method == "POST":
        key = request.POST["key"]

    if key is None:
        return HOME_VIEWS.index(request)
    else:
        return beerDetailInfo(request, key)

def beerDetailInfo(request, key):
    c = {}
    beer = SERVICES.selectBeerById(key)
    beer_taste_avg = SERVICES.selectBeerTasteAvgByBeer(beer)
    comment_list = list(SERVICES.selectCommentListByBeer(beer))
    del comment_list[20:]
    venue_list = list(SERVICES.selectVenueListByBeer(beer))
    del venue_list[20:]
    c.update({'beer':beer})
    c.update({'brewery':beer.brewery})
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
