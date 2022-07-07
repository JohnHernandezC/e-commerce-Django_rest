from Apps.products.models import *
from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta: 
     model = MeasureUnit
     exclude =('state','deleted_at','modified_at','created_at')
class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta: 
     model = CategoryProduct
     exclude =('state','deleted_at','modified_at','created_at')

class IndicadorSerializer(serializers.ModelSerializer):
    class Meta: 
     model = Indicator
     exclude =('state','deleted_at','modified_at','created_at')