from django.core.management.base import BaseCommand
from core import configs as CONFIG
import common.models as MODELS
import common.services as COMMON_SERVICES
import feedparser

"""
コマンドラインより $ python manage.py getnewsfeed　で実行可能。
cronにより定期実行する。
"""
class Command(BaseCommand):
    def handle(self, *args, **options):
        urls = CONFIG.NEWS_FEED_URLS
        urls_general = CONFIG.NEWS_FEED_URLS_GENERAL
        MODELS.NewsFeed.objects.filter().delete()
        for url in urls:
            feedpars = feedparser.parse(url)
            for feed in feedpars.entries:
                saveFeedNews(feedpars, feed)

        for url in urls_general:
            feedpars = feedparser.parse(url)
            for feed in feedpars.entries:
                if 'ビール' in feed['title']:
                    saveFeedNews(feedpars, feed)
                elif 'ブルワリー' in feed['title']:
                    saveFeedNews(feedpars, feed)
                elif 'つくば' in feed['title']:
                    saveFeedNews(feedpars, feed)


def saveFeedNews(feedpars, feed):
    try:
        entry = MODELS.NewsFeed()
        entry.site_name = feedpars.feed['title']
        entry.link = feed['link']
        entry.title = feed['title']
        entry.date = COMMON_SERVICES.parseDate(feed['updated_parsed'] or entry['published_parsed'])
        try:
            entry.photo = feed['href']
        except:
            pass
        entry.save()
    except:
        return
