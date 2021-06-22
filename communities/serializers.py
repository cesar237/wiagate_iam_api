from rest_framework import serializers
from .models import *


class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'
        read_only_fields = ['created_at', 'description']
