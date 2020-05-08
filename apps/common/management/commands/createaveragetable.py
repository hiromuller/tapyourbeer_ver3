from django.core.management.base import BaseCommand
from decimal import Decimal
import common.models as MODELS

"""
コマンドラインより $ python manage.py createaveragetable　で実行可能。
cronにより定期実行する。
"""
class Command(BaseCommand):
    def handle(self, *args, **options):
        beer_list = MODELS.Beer.objects.filter(is_active=True)
        MODELS.BeerTasteAvg.objects.all().delete()
        for beer in beer_list:
            comment_list = MODELS.Comment.objects.filter(beer=beer.id)
            if len(comment_list)==0:
                continue

            overall = []
            bitterness = []
            aroma = []
            body = []
            drinkability = []
            pressure = []
            specialness = []
            for comment in comment_list:
                overall.append(comment.overall)
                bitterness.append(comment.bitterness)
                aroma.append(comment.aroma)
                body.append(comment.body)
                drinkability.append(comment.drinkability)
                pressure.append(comment.pressure)
                specialness.append(comment.specialness)
            beerTasteAvg = MODELS.BeerTasteAvg(
                                            beer=beer,
                                            overall=getAverage(overall),
                                            bitterness=getAverage(bitterness),
                                            aroma=getAverage(aroma),
                                            body=getAverage(body),
                                            drinkability=getAverage(drinkability),
                                            pressure=getAverage(pressure),
                                            specialness=getAverage(specialness))
            beerTasteAvg.save()
            print (str(beerTasteAvg.beer.name) + 'の総合評価は' + str(beerTasteAvg.overall) + 'です。')



def getAverage(list):
    if list:
        return Decimal(sum(list)/len(list)).quantize(Decimal("0.01"))
    else:
        return 0
