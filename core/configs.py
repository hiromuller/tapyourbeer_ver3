# -*- coding: utf-8 -*-
"""
URL設定
"""
HOME_PAGE_TITLE_URL = 'home/page_title.html'
HOME_MAIN_URL = 'home/main_content.html'
HOME_SUB_URL = 'home/sub_content.html'

SIGNUP_MAIN_URL = 'common/signup.html'

BEER_PAGE_TITLE_URL = 'beer/page_title.html'
BEER_MAIN_URL = 'beer/main_content.html'
BEER_SUB_URL = 'beer/sub_content.html'

ADD_BEER_EVALUATION_PAGE_TITLE_URL = 'beer/add_page_title.html'
ADD_BEER_EVALUATION_MAIN_URL = 'beer/add_main_content.html'
ADD_BEER_SUB_URL = 'beer/add_sub_content.html'

BREWERY_PAGE_TITLE_URL = 'brewery/page_title.html'
BREWERY_MAIN_URL = 'brewery/main_content.html'
BREWERY_SUB_URL = 'brewery/sub_content.html'

MANAGER_PAGE_TITLE_URL = 'manager/page_title.html'
MANAGER_MAIN_URL = 'manager/main_content.html'
MANAGER_SUB_URL = 'manager/sub_content.html'

SEARCH_PAGE_TITLE_URL = 'search/page_title.html'
SEARCH_MAIN_URL = 'search/main_content.html'
SEARCH_SUB_URL = 'search/sub_content.html'
SEARCH_BAR_URL = 'search/search_bar.html'

DETAIL_SEARCH_PAGE_TITLE_URL = 'detail_search/page_title.html'
DETAIL_SEARCH_MAIN_URL = 'detail_search/main_content.html'
DETAIL_SEARCH_SUB_URL = 'detail_search/sub_content.html'
DETAIL_SEARCH_BAR_URL = 'detail_search/search_bar.html'

NEWS_PAGE_TITLE_URL = 'news/page_title.html'
NEWS_MAIN_URL = 'news/main_content.html'
NEWS_SUB_URL = 'news/sub_content.html'


USER_PAGE_TITLE_URL = 'user/page_title.html'
USER_MAIN_URL = 'user/main_content.html'
USER_SUB_URL = 'user/sub_content.html'
USER_UPDATE_URL = 'user/edit.html'
USER_FOLLOW_INFO_URL = 'user/follow_info.html'

VENUE_PAGE_TITLE_URL = 'venue/page_title.html'
VENUE_MAIN_URL = 'venue/main_content.html'
VENUE_SUB_URL = 'venue/sub_content.html'

TOP_URL = '/main/'
TOP_PAGE_TITLE = HOME_PAGE_TITLE_URL
TOP_CONTENT_MAIN = HOME_MAIN_URL
TOP_CONTENT_SUB = HOME_SUB_URL


"""
アクションの設定
"""
#home機能
ACTION_HOME = 'home'
#アカウント機能
ACTION_SIGNUP = 'signup'
ACTION_SIGNUP_USER = 'signup_user'
#beer機能
ACTION_BEER_DETAIL = 'beer_detail'
ACTION_ADD_BEER_EVALUATION_FORM = 'add_beer_evaluation_form'
ACTION_ADD_BEER_EVALUATION = 'add_beer_evaluation'
#brewery機能
ACTION_BREWERY_DETAIL = 'brewery_detail'
#search機能
ACTION_SEARCH = 'search' #検索画面へ遷移
ACTION_SEARCH_LIST = 'search_list' #検索実行
#detailsearch機能
ACTION_DETAIL_SEARCH = 'detail_search' #詳細検索画面へ遷移
ACTION_DETAIL_SEARCH_LIST = 'detail_search_list' #詳細検索実行
#news機能
ACTION_NEWS = 'news'
#user機能
ACTION_USER_ACCOUNT = 'user_account'
ACTION_USER_UPDATE = 'user_update' #ユーザ情報編集画面へ遷移
ACTION_UPDATE_USER = 'update_user' #ユーザ情報を編集し、ユーザ詳細画面へ遷移
ACTION_FOLLOW = 'follow'
ACTION_UNFOLLOW = 'unfollow'
ACTION_FOLLOW_INFO = 'follow_info'
ACTION_FOLLOWER_INFO = 'follower_info'
#venue機能
ACTION_VENUE_DETAIL = 'venue_detail'
#manager機能
ACTION_MANAGER_ACCOUNT = 'manager_account'
ACTION_DELETE_BEER = 'delete_beer'
ACTION_DELETE_USER = 'delete_user'
ACTION_DELETE_BREWERY = 'delete_brewery'
ACTION_DELETE_VENUE = 'delete_venue'
ACTION_DELETE_COMMENT = 'delete_comment'
ACTION_BEER_UPDATE = 'beer_update' #ビール更新画面へ遷移
ACTION_UPDATE_BEER = 'update_beer' #ビール情報を更新してビール詳細画面へ遷移
ACTION_BREWERY_UPDATE = 'brewery_update' #ブルワリー更新画面へ遷移
ACTION_UPDATE_BREWERY = 'update_brewery' #ブルワリー情報を更新してブルワリー詳細画面へ遷移
ACTION_BEER_MERGE = 'beer_merge' #ビール統合画面へ遷移
ACTION_MERGE_BEER = 'merge_beer' #ビール情報を統合してビール詳細画面へ遷移
ACTION_BREWERY_MERGE = 'brewery_merge' #ブルワリー統合画面へ遷移
ACTION_MERGE_BREWERY = 'merge_brewery' #ブルワリー情報を統合してブルワリー詳細画面へ遷移
ACTION_VENUE_UPDATE = 'venue_update' #店舗更新画面へ遷移
ACTION_UPDATE_VENUE = 'update_venue' #店舗情報を更新してビール詳細画面へ遷移
ACTION_UNTOUCHED_BREWERY = 'untouched_brewery' #未編集のブルワリー一覧を表示
ACTION_UNTOUCHED_BEER = 'untouched_beer' #未編集のビール一覧を表示

ACTION_DICT = {
                'ACTION_HOME':ACTION_HOME,
                'ACTION_SIGNUP':ACTION_SIGNUP,
                'ACTION_SIGNUP_USER':ACTION_SIGNUP_USER,
                'ACTION_BEER_DETAIL':ACTION_BEER_DETAIL,
                'ACTION_ADD_BEER_EVALUATION_FORM':ACTION_ADD_BEER_EVALUATION_FORM,
                'ACTION_ADD_BEER_EVALUATION':ACTION_ADD_BEER_EVALUATION,
                'ACTION_BREWERY_DETAIL':ACTION_BREWERY_DETAIL,
                'ACTION_MANAGER_ACCOUNT':ACTION_MANAGER_ACCOUNT,
                'ACTION_SEARCH':ACTION_SEARCH,
                'ACTION_SEARCH_LIST':ACTION_SEARCH_LIST,
                'ACTION_DETAIL_SEARCH':ACTION_DETAIL_SEARCH,
                'ACTION_DETAIL_SEARCH_LIST':ACTION_DETAIL_SEARCH_LIST,
                'ACTION_NEWS':ACTION_NEWS,
                'ACTION_USER_ACCOUNT':ACTION_USER_ACCOUNT,
                'ACTION_USER_UPDATE':ACTION_USER_UPDATE,
                'ACTION_UPDATE_USER':ACTION_UPDATE_USER,
                'ACTION_FOLLOW':ACTION_FOLLOW,
                'ACTION_UNFOLLOW':ACTION_UNFOLLOW,
                'ACTION_FOLLOW_INFO':ACTION_FOLLOW_INFO,
                'ACTION_FOLLOWER_INFO':ACTION_FOLLOWER_INFO,
                'ACTION_VENUE_DETAIL':ACTION_VENUE_DETAIL,
                'ACTION_DELETE_BEER':ACTION_DELETE_BEER,
                'ACTION_DELETE_USER':ACTION_DELETE_USER,
                'ACTION_DELETE_BREWERY':ACTION_DELETE_BREWERY,
                'ACTION_DELETE_VENUE':ACTION_DELETE_VENUE,
                'ACTION_DELETE_COMMENT':ACTION_DELETE_COMMENT,
                'ACTION_BEER_UPDATE':ACTION_BEER_UPDATE,
                'ACTION_UPDATE_BEER':ACTION_UPDATE_BEER,
                'ACTION_BREWERY_UPDATE':ACTION_BREWERY_UPDATE,
                'ACTION_UPDATE_BREWERY':ACTION_UPDATE_BREWERY,
                'ACTION_BEER_MERGE':ACTION_BEER_MERGE,
                'ACTION_MERGE_BEER':ACTION_MERGE_BEER,
                'ACTION_BREWERY_MERGE':ACTION_BREWERY_MERGE,
                'ACTION_MERGE_BREWERY':ACTION_MERGE_BREWERY,
                'ACTION_VENUE_UPDATE':ACTION_VENUE_UPDATE,
                'ACTION_UPDATE_VENUE':ACTION_UPDATE_VENUE,
                'ACTION_UNTOUCHED_BREWERY':ACTION_UNTOUCHED_BREWERY,
                'ACTION_UNTOUCHED_BEER':ACTION_UNTOUCHED_BEER,
               }
"""
コンテンツHTML
"""
PAGE_TITLE = '/page_title.html'
CONTENT_MAIN = '/main_content.html'
CONTENT_SUB = '/sub_content.html'

"""
HTMLタイトル
"""
HOME_HTML_TITLE = 'Home'
NEWS_HTML_TITLE = 'News'
SIGNUP_HTML_TITLE = 'Signup'
BEER_HTML_TITLE = 'Beer'
ADD_BEER_EVALUATION_HTML_TITLE = 'Add Beer'
BREWERY_HTML_TITLE = 'Brewery'
MANAGER_HTML_TITLE = 'Manager'
USER_HTML_TITLE = 'User'
SEARCH_HTML_TITLE = 'Search'
DETAIL_SEARCH_HTML_TITLE = 'Detail Search'
VENUE_HTML_TITLE = 'Venue'

"""
ニュースフィード取得元
"""
#クラフトビール関連のサイト
NEWS_FEED_URLS = [
                'https://www.jbja.jp/feed',
                'https://craftbeer-tokyo.info/feed/',
                'https://note.com/bestbeerjapan/rss',
                'https://mycraftbeers.com/feed',
                ]

#一般的なサイト
NEWS_FEED_URLS_GENERAL = [
                        'https://headlines.yahoo.co.jp/rss/all-dom.xml',
                        'https://headlines.yahoo.co.jp/rss/all-c_int.xml',
                        'https://headlines.yahoo.co.jp/rss/all-bus.xml',
                        'https://headlines.yahoo.co.jp/rss/all-c_ent.xml',
                        'https://headlines.yahoo.co.jp/rss/all-c_spo.xml',
                        'https://headlines.yahoo.co.jp/rss/all-c_sci.xml',
                        'https://headlines.yahoo.co.jp/rss/all-c_life.xml',
                        'https://headlines.yahoo.co.jp/rss/all-loc.xml',
                        'https://headlines.yahoo.co.jp/rss/newstkb-loc.xml',
]
