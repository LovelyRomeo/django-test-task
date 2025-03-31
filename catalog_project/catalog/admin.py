from django.contrib import admin
from .models import Product, Image, Parameter

class ImageInline(admin.TabularInline):                                     #Импорт модели в адлмин панель
    model = Image                                                           #Базовое кол-во фото
    extra = 1

class ParameterInline(admin.TabularInline):                                 #Импорт модели в адлмин панель
    model = Parameter
    extra = 1                                                               #Базовое кол-во параметров

@admin.register(Product)                                                    #Регистрируем админ-панель
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ParameterInline]
