from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from Apps.users.models import User
from Apps.users.api.serializers import UserSerializer,UserListSerializer

# class UserAPIView(APIView):
#     def get(self, request):
#         users=User.objects.all()
#         users_serializer=UserSerializer(users, many=True)
#         # many es para definir que se ban a devolver varios
#         return Response(users_serializer.data)

@api_view(['GET','POST'])
def users_api_view(request):
    if request.method == 'GET':
        users=User.objects.all().values('id','username','email','password')
        users_serializer=UserListSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        user_serializer=UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def users_detail_view(request,pk):
    #queryset
    user=User.objects.filter(id=pk).first()
    #validacion
    if user:
        if request.method == 'GET':
            user_serializer=UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            user_serializer=UserSerializer(user,data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_404_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Usuario eliminado correctamente'}, status=status.HTTP_200_OK)
    return Response({'message':'No se ha encontrado un usuario con estos datos'},status=status.HTTP_404_BAD_REQUEST)        
            