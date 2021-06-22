from rest_framework import viewsets
from .models import *
from .serializers import *


class EquipmentModelViewSet(viewsets.ModelViewSet):
    queryset = EquipmentModel.objects.all()
    serializer_class = EquipmentModelSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationProfileViewSet(viewsets.ModelViewSet):
    queryset = ApplicationProfile.objects.all()
    serializer_class = ApplicationProfileSerializer

