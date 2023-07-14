from django.db import models
from django.core import validators
# Create your models here.

class Item(models.Model):
    
    name = models.CharField(
        verbose_name='名前',
          max_length=20,
    )
    phone = models.CharField(
        verbose_name='電話番号',
        max_length=13,
    )
  
    product = models.CharField(
        verbose_name='商品の名前',
        max_length=50,
    )
    jan = models.CharField(
        verbose_name='janコード',
        max_length=15,
    )
    staff = models.CharField(
        verbose_name='担当者',
        max_length=10,
    )
    setcardID = models.CharField(
        verbose_name='カードID',
        max_length=10,

    )
    created_at = models.DateTimeField(
        verbose_name='予約日',
        auto_now_add=True
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'



