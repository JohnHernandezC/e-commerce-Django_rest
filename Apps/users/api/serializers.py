from unicodedata import name
from rest_framework import serializers
from Apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        
    def create(self, validated_data):
        user=User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    def update(self,instance, validated_data):
        update_user= super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user
        
    

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        
        
    def to_representation(self,instance):#instance es donde estan amacenados los valores
        return{
            'id':instance['id'],
            'username':instance['username'],
            'email':instance['email'],
            'password':instance['password']
        }
    
# class TestUserSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     email=serializers.EmailField()
    
#     def validate_name(self, value):
#         pass
#     def validate_email(self, value):
#         pass
#     def validate(self, value):
#         pass
#     def update (self, instance, validated_data):
#         pass

