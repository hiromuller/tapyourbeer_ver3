from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from core import consts as CONST

# Create your models here.
class Brewery(models.Model):
    """
    ブルワリーモデル
    """
    def __unicode__(self):
        return self.name
    # 名前
    name = models.CharField(max_length=200)
    # logo
    logo = models.ImageField(upload_to='images/', null=True, blank=True)
    # 住所
    address = models.CharField(max_length=200, null=True, blank=True)
    # 説明
    description = models.CharField(max_length=200, null=True, blank=True)
    #アクティブか非アクティブか
    is_active = models.BooleanField(default=True)

    def encode(self):
        return {
            'name': self.name,
            'logo': self.logo,
            'address': self.address,
            'description': self.description,
            'is_active': self.is_active,
        }

class Beer(models.Model):
    """
    ビールモデル
    """
    def __unicode__(self):
        return self.name
    # 名前
    name = models.CharField(max_length=200)
    # style
    style = models.CharField(max_length=200, null=True, blank=True)
    # 説明
    description = models.CharField(max_length=200, null=True, blank=True)
    # ibu（苦さ）
    ibu = models.CharField(max_length=200, null=True, blank=True)
    # abv（アルコール度数）
    abv = models.CharField(max_length=200, null=True, blank=True)
    # ブルワリー
    brewery = models.ForeignKey(Brewery, on_delete=models.PROTECT)
    # photo (画像）
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    # アクティブか非アクティブか
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('name', 'brewery')

    def encode(self):
        return {
                'name': self.name,
                'style': self.style,
                'description': self.description,
                'ibu': self.ibu,
                'abv': self.abv,
                'brewery': self.team.encode(),
                'photo': self.photo,
                'is_active': self.is_active,
                }

class Venue(models.Model):
    """
    店モデル
    """
    #ぐるなびID
    gurunavi_id = models.IntegerField(null=True)
    # 名前
    name = models.CharField(max_length=200)
    # アクティブか非アクティブか
    is_active = models.BooleanField(default=True)

    def encode(self):
        return {
            'gurunavi_id': self.gurunavi_id,
            'name': self.name,
        }

class TodaysTap(models.Model):
    """
    本日のタップモデル
    """
    # 店
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT)
    # ビール
    beer = models.ForeignKey(Beer, on_delete=models.PROTECT)
    # 登録日
    registered_date = models.DateTimeField(default=timezone.now)
    # アクティブか非アクティブか
    is_active = models.BooleanField(default=False)

    def encode(self):
        return {
            'venue': self.venue.encode(),
            'beer': self.beer.encode(),
            'registered_date': self.registered_date,
            'is_active': self.is_active,
        }

class CustomUser(AbstractUser):
    """
    ユーザー拡張モデル
    """
    # djangoユーザモデル
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 性別スタイル
    gender_style = models.CharField(max_length=200, choices=CONST.GENDER_STYLE_CHOICES, null=True, blank=True)
    # 誕生日
    birthday = models.DateField(null=True, blank=True)
    # 住んでいる国
    living_country = models.CharField(max_length=200, choices=CONST.COUNTRY_CHOICES, null=True, blank=True)
    # 住んでいる地域
    living_area = models.CharField(max_length=200, null=True, blank=True)
    # アプリ管理者
    is_admin = models.BooleanField(default=False)
    # ブルワリー管理者
    is_managing_brewery = models.BooleanField(default=False)
    # 店舗管理者
    is_managing_venue = models.BooleanField(default=False)
    # 画像
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    # ユーザランク
    user_rank = models.IntegerField(default=1, choices=CONST.USER_RANK_CHOICES)
    # ユーザ紹介
    description = models.CharField(max_length=200, null=True, blank=True)
    """
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    """

class Comment(models.Model):
    """
    味評価モデル
    """
    # ビール
    beer = models.ForeignKey(Beer, on_delete=models.PROTECT)
    # コメントしたユーザ
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    # 提供している店
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True)
    # 画像
    photo = models.ImageField(upload_to='images/', null=True)
    # 苦味
    bitterness = models.IntegerField(choices=CONST.EVALUATION_CHOICES_STRONGNESS)
    # 香り
    aroma = models.IntegerField(choices=CONST.EVALUATION_CHOICES_STRONGNESS)
    # ボディ
    body= models.IntegerField(choices=CONST.EVALUATION_CHOICES_EXISTNESS)
    # 飲みやすさ
    drinkability = models.IntegerField(choices=CONST.EVALUATION_CHOICES_GOODNESS)
    # 圧
    pressure = models.IntegerField(choices=CONST.EVALUATION_CHOICES_STRONGNESS)
    # 苦味
    specialness = models.IntegerField(choices=CONST.EVALUATION_CHOICES_EXISTNESS)
    # 総合
    overall = models.IntegerField(choices=CONST.EVALUATION_CHOICES_GOODNESS)
    # コメント
    comment = models.CharField(max_length=200, null=True)
    # 登録日
    registered_date = models.DateTimeField(default=timezone.now)

    def encode(self):
        return {
            'beer': self.beer.encode(),
            'user': self.user.encode(),
            'venue': self.venue.encode(),
            'photo': self.photo,
            'bitterness': self.bitterness,
            'aroma': self.aroma,
            'body': self.body,
            'drinkability': self.drinkability,
            'pressure': self.pressure,
            'specialness': self.specialness,
            'overall': self.overall,
            'comment': self.comment,
        }

class Follow(models.Model):
    """
    フォローモデル
    """
    # ユーザ
    user = models.ForeignKey(CustomUser, related_name='following_user', on_delete=models.CASCADE)
    # フォロー
    follow = models.ForeignKey(CustomUser, related_name='followed_user', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'follow')


class TCBFParticipant(models.Model):
    """
    TCBF参加ブルワリーモデル
    """
    # ブルワリー
    brewery = models.ForeignKey(Brewery, on_delete=models.PROTECT)
    # 参加年度
    year = models.IntegerField()

    class Meta:
        unique_together = ('brewery', 'year')

class BreweryManager(models.Model):
    """
    ブルワリー管理者モデル
    """
    # ブルワリー
    brewery = models.ForeignKey(Brewery, on_delete=models.PROTECT)
    # ユーザー
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('brewery', 'user')

class VenueManager(models.Model):
    """
    店舗管理者モデル
    """
    # 店舗
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT)
    # ユーザー
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('venue', 'user')

class Like(models.Model):
    """
    いいねモデル
    """
    #　コメント
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # ユーザー
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('comment', 'user')

class BeerTasteAvg(models.Model):
    """
    ビールの味わい平均値モデル
    """
    # ビール
    beer = models.ForeignKey(Beer, unique=True, on_delete=models.CASCADE)
    # 苦味
    bitterness = models.DecimalField(max_digits=3, decimal_places=2)
    # 香り
    aroma = models.DecimalField(max_digits=3, decimal_places=2)
    # ボディ
    body= models.DecimalField(max_digits=3, decimal_places=2)
    # 飲みやすさ
    drinkability = models.DecimalField(max_digits=3, decimal_places=2)
    # 圧
    pressure = models.DecimalField(max_digits=3, decimal_places=2)
    # 苦味
    specialness = models.DecimalField(max_digits=3, decimal_places=2)
    # 総合
    overall = models.DecimalField(max_digits=3, decimal_places=2)


admin.site.register(Beer)
admin.site.register(Brewery)
admin.site.register(Venue)
admin.site.register(Comment)
admin.site.register(TodaysTap)
admin.site.register(Follow)
admin.site.register(TCBFParticipant)
admin.site.register(BreweryManager)
admin.site.register(VenueManager)
admin.site.register(Like)
admin.site.register(BeerTasteAvg)
#test
