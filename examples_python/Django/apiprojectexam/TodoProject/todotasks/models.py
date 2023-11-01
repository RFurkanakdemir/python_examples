from django.db import models
import datetime 

# Create your models here.

class Task(models.Model):
    cok_onemli='Çok önemli'
    önemli='Önemli'
    normal='Normal'
    aciliyeti_yok='aciliyeti yok'
    önemsiz='önemsiz'
    oncelikler = [
        (cok_onemli ,'çok önemli'),
        (önemli  ,'önemli'),
        (normal  ,'normal'),
        (aciliyeti_yok  ,'aciliyeti yok'),
        (önemsiz ,'önemsiz'),
    ]
    


    oncelik=models.CharField(
        max_length=13,
        choices=oncelikler,
        default=normal,
    )
    icerik=models.TextField(max_length=500,default='görevi giriniz',blank=True)
    bas_tarih = models.DateTimeField(default=datetime.datetime.now())
    bit_tarih = models.DateTimeField(default=datetime.datetime.now())
    is_active = models.BooleanField(default=True)
    # z=datetime.datetime.strptime(bas_tarih,'%Y-%B-%dT%H:%M:%SZ')
    # y=datetime.datetime.strptime(bit_tarih,'%Y-%B-%dT%H:%M:%SZ')
    # fark=z-y
    # kalan_süre=models.BigAutoField(
    #     read_only=True
    #     default='fark'
    # )

    def __str__(self):
        return self.oncelik