from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    picture = models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=200)
    is_provider = models.BooleanField(default=False)
    tel = models.CharField(max_length=200)
    sp_profile = models.OneToOneField('users.ServiceProviderProfile', on_delete=models.SET_NULL, null=True)


class ServiceProviderProfile(User):
    pass