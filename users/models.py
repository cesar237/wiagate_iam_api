from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    picture = models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=200)
    is_provider = models.BooleanField(default=False)
    tel = models.CharField(max_length=200)


class ServiceProviderProfile(models.Model):
    user = models.ForeignKey('users.User', related_name='profile_owner', on_delete=models.CASCADE, null=True)
