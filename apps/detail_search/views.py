# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import configs as CONFIG
from core import consts as CONSTS
from core import messages as MSG
from core import settings as SETTING
import detail_search.services as SERVICES
import detail_search.forms as FORMS
import logging

logger = logging.getLogger('app')

def detailSearchList(request):
    logger.info('detail_search_list')
    c = {}

    if request.method == "POST" and FORMS.detailSearchForm(request.POST).is_valid():
        form = FORMS.detailSearchForm(request.POST)
        detail_search_form = {'detail_search_form':form}
        c.update(detail_search_form)

        is_valid_detail_search_form_condition = SERVICES.validateDetailSearchFormCondition(form)

        if is_valid_detail_search_form_condition:
            keys = {'overall':form.cleaned_data['overall'],
                    'bitterness':form.cleaned_data['bitterness'],
                    'aroma':form.cleaned_data['aroma'],
                    'body':form.cleaned_data['body'],
                    'drinkability':form.cleaned_data['drinkability'],
                    'pressure':form.cleaned_data['pressure'],
                    'specialness':form.cleaned_data['specialness'],
                    }
            search_result_beer_list = SERVICES.selectDetailSearchResultList(keys)
            c.update({'beer_list':search_result_beer_list})
            if len(search_result_beer_list) == 0:
                c.update({'no_search_result':MSG.RESULT_NOT_FOUND})
        else:
            c.update({'form_message':MSG.PLEASE_INSERT_KEYS})
    else:
        return index(request)

    return showDetailSearch(request, c)

def index(request):
    logger.info('detail_search')
    c = {}

    detail_search_form = {'detail_search_form':FORMS.detailSearchForm()}

    c.update(detail_search_form)
    return showDetailSearch(request, c)


def showDetailSearch(request, c):
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
