from rest_framework import generics
from Apps.products.models import *
from Apps.base.api import generalListAPIView
from Apps.products.api.serializers.generalSerializers import *

class MeasureUnitListAPIView (generalListAPIView):
    #lo que se hizo fue heredar de una classe que creamos generica que nos muestre para mostrar todas las listas
    serializer_class =MeasureUnitSerializer
    #solo es necesario enviar el serializador


class IndicatorListAPIView (generics.ListAPIView):
    serializer_class =IndicadorSerializer
   

class CategoryProductListAPIView (generics.ListAPIView):
    serializer_class =CategoryProductSerializer
    #la vista generica internamente obtiene los valores sy los agrega al serializador
    def get_queryset(self):
        return CategoryProduct.objects.filter(state=True)   
    




