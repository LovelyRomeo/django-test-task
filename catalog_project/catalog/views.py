from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, Parameter 
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()                                               #Фильтрация по 'name', 'value' и 'price'
        name = self.request.query_params.get('name', None)                              
        value = self.request.query_params.get('value', None)                            
        price = self.request.query_params.get('price', None)                            
        
        if name:                                                                        #Фильтрация по названию товара
            queryset = queryset.filter(name__icontains=name)        
        if value:                                                                       #Фильтрация по значению параметра
            queryset = queryset.filter(parameters__value=value)
        if price is not None:                                                           #Фильтрация по цене
            queryset = queryset.filter(price=price)
        return queryset

    def list(self, request, *args, **kwargs):                                           #Даём параметрам 'понять', в скольки продуктах он есть       
        queryset = self.get_queryset()
        products_data = self.get_serializer(queryset, many=True).data

        parameter_count = {}                                                            #Создание пустого словаря    
        for product in queryset:                                                        #Цикл в цикле, в цикле дающий 'осознание' параметрам 
            for param in product.parameters.all():
                if param.name not in parameter_count:
                    parameter_count[param.name] = set() 
                parameter_count[param.name].add(product.id) 
        parameter_count = {param: len(product_ids) for param, product_ids in parameter_count.items()}       #Полчаем итоговое число
        response_data = {
            'products': products_data,
            'parameter_count': parameter_count,
        }

        return Response(response_data)                                          

    @action(detail=False, methods=['get'])                                               #доп. метод для создания маршрута филтрации
    def filter_parameters(self, request):
        parameters = Parameter.get_filter_parameters() 
        return Response(parameters)