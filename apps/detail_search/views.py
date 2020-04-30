# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import configs as CONFIG
from core import consts as CONSTS
from core import settings as SETTING
import detail_search.services as SERVICES
import detail_search.forms as FORMS
import logging

logger = logging.getLogger('app')

def index(request):
    logger.info('detail_search')
    c = {}

    #検索リクエストが入っていない場合
    detail_search_form = {'detail_search_form':FORMS.detailSearchForm()}

    #検索リクエストが入っていた場合
    detail_search_form = {'detail_search_form':FORMS.detailSearchForm(request)}
    #detail_search_result = SERVICES.detailSearch()

    """
    味わい詳細検索算出
    １．それぞれの味わい指標の誤差の点数を決める（ピタリマッチだと０点、プラマイ0.5だと１点、プラマイ１だと２点）
    ２．指定した指標が１項目のみの場合、０点のデータをセレクト、なければ１点、それでもなければ２点と検索を増やしていく。検索結果が50件貯まるか、最大点数の8点の検索が終了したら検索終了。
    ２．指定した指標が２項目の場合、２項目で誤差０点のデータをセレクトし、なければ１点（つまり誤差はプラマイ0.25）、それでもなければ２点で、検索結果が５０件貯まるか最大点数の１６点の検索が終了したら検索終了。
    ２．指定した指標が３項目の場合、２項目の場合と同様の点数処理を行う。

    #１項目の場合
    指標　誤差　点数
    1 0 0
    1.5 0.5 1
    2   1   2
    2.5 1.5 3
    3   2   4
    3.5 2.5 5
    4   3   6
    4.5 3.5 7
    5   4   8

    ３．データのセレクトは公平性を保つためにランダム順にする。（あえてランダム順処理を入れる）
    """

    c.update(detail_search_form)
    return showDetailSearch(request, c)


def showDetailSearch(request, c):
#def index(request):
#    logger.info('detail_search')
#    c = {}
    main_url = CONFIG.TOP_URL
    page_title = CONFIG.DETAIL_SEARCH_PAGE_TITLE_URL
    main_content = CONFIG.DETAIL_SEARCH_MAIN_URL
    sub_content = CONFIG.DETAIL_SEARCH_SUB_URL
    search_bar = CONFIG.DETAIL_SEARCH_BAR_URL
    action_dict = CONFIG.ACTION_DICT
    url_dict = {'main_url':main_url,
                'page_title':page_title,
                'main_content':main_content,
                'sub_content':sub_content,
                'search_bar':search_bar,
                }
    c.update({'html_title':CONFIG.DETAIL_SEARCH_HTML_TITLE})
    c.update({'move_to_search_button':True})
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)
