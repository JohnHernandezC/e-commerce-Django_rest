from django.urls import path
from  Apps.users.api.views import  users_api_view, users_detail_view
#from  Apps.users.api.views import UserAPIView 
urlpatterns = [
    path('usuarios/',users_api_view, name='usuarios-Api'),
    path('usuarios/<int:pk>',users_detail_view, name='usuarios-detail-Api')
    #path('usuarios/',UserAPIView.as_view(), name='usuarios-Api')
]