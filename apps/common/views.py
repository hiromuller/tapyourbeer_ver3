# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from core import consts as CONST
#import consts as CONST
from core import configs as CONFIG
from core import settings as SETTING
import common.services as SERVICES
import home.views as HOME_VIEWS
import login.views as LOGIN_VIEWS
import beer.views as BEER_VIEWS
import brewery.views as BREWERY_VIEWS
import manager.views as MANAGER_VIEWS
import search.views as SEARCH_VIEWS
import user.views as USER_VIEWS
import venue.views as VENUE_VIEWS
import logging
logger = logging.getLogger('app')

#@login_required(login_url='/login/')
def index(request):
    #暫定的にsessionユーザを定義。あとで消す
#    test_user = SERVICE.getUserByLoginId('user1')
#    request.session['user'] = test_user
    #ここまで
    """
    if request.method == "POST":
        action = request.POST["action"]
    else:
        action = CONFIG.ACTION_LOGIN

    if request.user.is_active:
        #ページの振り分け
        if action == CONFIG.ACTION_HOME:
            return HOME_VIEWS.index(request)
        #ここにelifでページを追加していく
    else:
        return view(request)
    """

#準備用
    action = request.POST["action"]
    print (action)
    if action == CONFIG.ACTION_HOME:
        return HOME_VIEWS.index(request)
    elif action == CONFIG.ACTION_BEER_DETAIL:
        return BEER_VIEWS.index(request)
    elif action == CONFIG.ACTION_ADD_BEER_EVALUATION:
        return BEER_VIEWS.show_add_beer_form(request)
    elif action == CONFIG.ACTION_BREWERY_DETAIL:
        return BREWERY_VIEWS.index(request)
    elif action == CONFIG.ACTION_LOGIN:
        return LOGIN_VIEWS.index(request)
    elif action == CONFIG.ACTION_MANAGER_ACCOUNT:
        return MANAGER_VIEWS.index(request)
    elif action == CONFIG.ACTION_SEARCH_LIST:
        return SEARCH_VIEWS.index(request)
    elif action == CONFIG.ACTION_USER_ACCOUNT:
        return USER_VIEWS.index(request)
    elif action == CONFIG.ACTION_VENUE_DETAIL:
        return VENUE_VIEWS.index(request)
    else:
        return view(request)

def view(request):
    return HOME_VIEWS.index(request)
#     main_url = CONFIG.TOP_URL
#     page_title = CONFIG.TOP_PAGE_TITLE
#     main_content = CONFIG.TOP_CONTENT_MAIN
#     sub_content = CONFIG.TOP_CONTENT_SUB
#
#     c = {}
#     url_dict = {'main_url':main_url,
#                 'page_title':page_title,
#                 'main_content':main_content,
#                 'sub_content':sub_content}
#     c.update(csrf(request))
#     c.update(url_dict)
#     c.update({'html_title':CONFIG.HOME_HTML_TITLE})
#     c.update(CONFIG.ACTION_DICT)
#     return render(request, 'common/main.html', c)
