from django.db import models
from decimal import *

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='Описание')
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='homework/', verbose_name='Фото', **NULLABLE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    # category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за штуку')
    date_of_creation = models.DateField(verbose_name='Дата создания')
    last_modified_date = models.DateField(verbose_name='Дата последнего изменения')
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
