"""wiagate_iam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from users.views import UserViewSet


# router = DefaultRouter()
# router.register('users', UserViewSet)

from rest_framework.decorators import api_view
from rest_framework.response import Response

root_url = "https://wiagate-iam-api.herokuapp.com"

@api_view(["GET"])
def api_root(request, format=None):
    """
    Retrouver le lien vers la vue par défaut des api
    """
    return Response({
        "User API": root_url + "/users_api/",
        "Service API": root_url + "/services_api/",
        "Community API": root_url + '/communities_api/',
        "OAUTH API": root_url + '/o/'
    })
    


urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users_api/', include('users.urls')),
    path('services_api/', include('services.urls')),
    path('communities_api/', include('communities.urls')),
#    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', api_root),
]

