from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from Apps.base.api import generalListAPIView
from Apps.products.api.serializers.productSerializers import ProductSerializer

class ProductListApiView(generalListAPIView):
    serializer_class=ProductSerializer
    
class ProductCreateApiView(generics.CreateAPIView):
    serializer_class=ProductSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'producto creado correctamente'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class productRetrievApiView(generics.RetrieveAPIView):
    serializer_class=ProductSerializer
    #usamos este metodo para buscar el modelo y filtrar por la pk que le estamos enviando
    def  get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    # def get(self,request,pk=None):
    #     se puede sobreescribir el get para recibir la pk y filtrar como en las vistas basadas en metodos
    
class ProducDestroyApiView(generics.DestroyAPIView):
    serializer_class=ProductSerializer
    def  get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    #Eliminacion logica
    # def delete(self,request,pk=None):
    #     product=self.get_queryset().filter(id=pk).first()
    #     if product:
    #         product.state=False
    #         product.save()
    #         return Response({'message':'Producto eliminado de manera correcta'},status=status.HTTP_200_OK)
    #     return Response({'error':'NOexiste producto con estos datos'},status=status.HTTP_400_BAD_REQUEST)
class ProductUpdateApiView(generics.UpdateAPIView):  
    serializer_class= ProductSerializer
    def  get_queryset(self,pk):
        return self.get_serializer().Meta.model.objects.filter(state=True).filter(id=pk).first()
    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            product_serializer=self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'NOexiste producto con estos datos'},status=status.HTTP_400_BAD_REQUEST)
    def put (self,request,pk=None):
        if self.get_queryset(pk):
            product_serializer=self.serializer_class(self.get_queryset(pk),data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    