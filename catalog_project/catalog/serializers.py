from rest_framework import serializers
from .models import Product, Parameter, Image

class ImageSerializer(serializers.ModelSerializer):             #Cериализер фото(отображение фото)
    class Meta:
        model = Image
        fields = ['file', 'caption']                            #Поля 'file' - 'ссылка на фото', 'caption' - 'подпись к фото'

class ParameterSerializer(serializers.ModelSerializer):         #Cериализер параметров(отображение параметров товара)
    unucal_params = serializers.SerializerMethodField()

    class Meta:
        model = Parameter
        fields = ['name', 'value', 'unucal_params']              #Поля 'name' - 'название параметра', 'value' - 'значение параметра', 'unucal_params' - 'все уникальные значения параметра'

    def get_unucal_params(self, obj):
        return Parameter.objects.filter(name=obj.name).values_list('value', flat=True).distinct()
    
class ProductSerializer(serializers.ModelSerializer):                   #Cериализер продукта(отображение всего продукта)
    images = ImageSerializer(many=True, read_only=True)                 #Помещаем ImageSerializer в переменную images
    parameters = ParameterSerializer(many=True, read_only=True)         #Помещаем ParameterSerializer в переменную parameters

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'images', 'parameters']       #Поля 'name' - 'название продукта', 'description' - 'price' - 'цена', 'images' - 'сериализер ImageSerializer', 'parameters' - 'сериализер ParameterSerializer'   

