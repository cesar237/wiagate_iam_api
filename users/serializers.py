from rest_framework import serializers
from .models import User, ServiceProviderProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username', 
            'first_name',
            'last_name',
            'email',
            'address', 
            'tel', 
            'is_provider', 
            'picture',
        ]
        read_only_fields = [
            'id',
            'is_provider',
        ]
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'email': {'required': False},
            'address': {'required': False},
            'tel': {'required': False},
            'picture': {'required': False},
        }

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name',
            'last_name',
            'email',
            'address', 
            'tel', 
            'picture',
            'password',
        ]
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'email': {'required': False},
            'address': {'required': False},
            'tel': {'required': False},
            'picture': {'required': False},
        }
        write_only_fields = {
            'password',
        }    

class ServiceProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username', 
            'first_name',
            'last_name',
            'email',
            'address', 
            'tel', 
            'is_provider', 
            'picture',
            'sp_profile',
        ]
        read_only_fields = [
            'id',
            'is_provider',
            'sp_profile',
        ]
