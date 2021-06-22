from rest_framework import serializers
from .models import *
from oauth2_provider.models import Application


class EquipmentModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EquipmentModel
        fields = '__all__'
        read_only_fields = ['__all__']


class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipment
        fields = [
            'url',
            'id',
            'model',
            'label',
            'registery_date',
            'community',
            'owner',
            'picture',
        ]
        read_only_fields = ['url', 'id', 'registery_date']


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class ApplicationProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApplicationProfile
        fields = '__all__'
