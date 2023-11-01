from django.db import models

# Create your models here.
class Makale(models.Model):
    yazar=models.CharField(max_length=200,default='some_value')
    baslik=models.CharField(max_length=200,default='some_value')
    aciklama=models.CharField(max_length=200,default='some_value')
    metin=models.TextField()
    sehir=models.CharField(max_length=200,default='some_value')
    yayinlanma_tarihi=models.DateField()
    aktif=models.BooleanField()
    # yaratilma_tarih=models.DateTimeField(auto_now_add=True)
    # güncellenme_tarihi=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.baslik



    