from django.db import models
from django.db.models import Count

class Product(models.Model):               #Модель товара
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_parameters(self):
        return self.parameters.all()

class Image(models.Model):                  #Модель изображения
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, verbose_name='Товар')
    file = models.ImageField(upload_to='media/', verbose_name='Файл изображения')
    caption = models.CharField(max_length=255, blank=True, verbose_name='Подпись')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

class Parameter(models.Model):                #Мподель параметров
    product = models.ForeignKey(Product, related_name='parameters', on_delete=models.CASCADE, verbose_name='Параметры')
    name = models.CharField(max_length=255, verbose_name='Название')
    value = models.CharField(max_length=255, verbose_name='Значение')
    file = models.ImageField(upload_to='media/', verbose_name='Файл изображения', blank=True, null=True,)

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'

    @classmethod                                
    def get_filter_parameters(cls):
        return cls.objects.values('name').annotate(
            unique_values=Count('value', distinct=True),
            product_count=Count('product', distinct=True)
        ).distinct()
