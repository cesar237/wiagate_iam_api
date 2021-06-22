from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('sp_profiles', ServiceProviderProfileViewSet)

urlpatterns = [
    path('users/<int:pk>/turn_to_provider/', turn_to_provider),
    path('providers_list/', ProviderListView.as_view()),
    path('login/', login),
    path('turn_to_provider/<int:pk>/', turn_to_provider),
    path('', include(router.urls)),
]
