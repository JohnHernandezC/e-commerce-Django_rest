from Apps.products.models import Product
from rest_framework import serializers
from Apps.products.api.serializers.generalSerializers import *

class ProductSerializer(serializers.ModelSerializer):
    # MeasureUnit=MeasureUnitSerializer()
    # categoryProduc=CategoryProductSerializer()
    #measureUnit= MeasureUnitSerializer(many=True, read_only=True )# Esto trae todos los datos
    
    #toma lo qeu esta en el str
    # MeasureUnit=serializers.StringRelatedField()
    # categoryProduc=serializers.StringRelatedField()
    
    #el nombre de la variable debe ser la misma de la llave foranea en la base de datos
    class Meta: 
     model = Product
     exclude =('state','deleted_at','modified_at','created_at')
     
    def to_representation(self,instance):
        return{
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image if instance.image !='' else '',
            'MeasureUnit': instance.MeasureUnit.description,
            'categoryProduc': instance.categoryProduc.description
        }
    def create(self, validated_data):
        if validated_data['image'] == None:
            validated_data['image'] = ''
        return Product.objects.create(**validated_data)
    
    #inmueblesList= serializers.PrimaryKeyRelatedField(many=True)#solo nos devuelve los id
    #inmueblesList= serializers.StringRelatedField(many=True)#solo nos devuelve lo que este en el str del modelo
    # inmueblesList= serializers.HyperlinkedRelatedField(
    #                         many=True,
    #                         read_only=True,
    #                         view_name='detalle'
    #     )#nos genera un lin hacia las entidades que pertenecen 