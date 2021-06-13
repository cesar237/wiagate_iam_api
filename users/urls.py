from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.SimpleRouter()
router.register('users/', UserViewSet)

urlpatterns = [
    path('users/<int:pk>/turn_to_provider/', turn_to_provider),
    path('providers/', ProviderListView.as_view()),
    path('login/', login)
#    path('', include(router.urls)),
]
