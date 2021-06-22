from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('equipment_models', EquipmentModelViewSet)
router.register('equipments', EquipmentViewSet)
router.register('applications', ApplicationViewSet)
router.register('application_profiles', ApplicationProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
