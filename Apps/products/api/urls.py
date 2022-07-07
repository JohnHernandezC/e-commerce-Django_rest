from django.urls import path
from  Apps.products.api.Views.generalViews import  *
from  Apps.products.api.Views.products_views import  *
#from  Apps.users.api.views import UserAPIView 
urlpatterns = [
    path('measure_unit/',MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('indicator/',IndicatorListAPIView.as_view(), name='indicator'),
    path('category_product/',CategoryProductListAPIView.as_view(), name='category_product'),
    path('product/',ProductListApiView.as_view(), name='product'),
    path('product/create',ProductCreateApiView.as_view(), name='product_create'),
    path('product/retrive/<int:pk>',productRetrievApiView.as_view(), name='product_Retrive'),
    path('product/destroy/<int:pk>',ProducDestroyApiView.as_view(), name='product_destroy'),
    path('product/update/<int:pk>',ProductUpdateApiView.as_view(), name='product_update'),
    #path('usuarios/',UserAPIView.as_view(), name='usuarios-Api')
]