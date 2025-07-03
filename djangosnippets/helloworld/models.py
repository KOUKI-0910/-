from django.conf import settings
from django.db import models

class Helloworld(models.Model):
    title = models.CharField('タイトル', max_length=128)
    problem_image = models.ImageField('自転車の写真', upload_to='problems/', blank=True, null=True)
    description = models.TextField('説明', blank=True)
    latitude = models.FloatField('緯度', blank=True, null=True)
    longitude = models.FloatField('経度', blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name='投稿者',
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField('投稿日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.title

class Shop(models.Model):
    name = models.CharField('店名', max_length=128)
    address = models.CharField('住所', max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField('説明', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name='投稿者',
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField('投稿日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.name

class Sighting(models.Model):
    theft_report = models.ForeignKey(Helloworld, related_name='sightings', on_delete=models.CASCADE, verbose_name='関連する盗難情報')
    sighting_location = models.CharField('目撃場所', max_length=100)
    sighting_datetime = models.DateTimeField('目撃日時')
    sighting_image = models.ImageField('写真', upload_to='sightings/', blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='報告者', on_delete=models.CASCADE)
    created_at = models.DateTimeField('報告日時', auto_now_add=True)

    def __str__(self):
        return f'{self.theft_report.title} の目撃情報 - {self.sighting_location}'
