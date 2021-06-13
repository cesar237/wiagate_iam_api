from django.db import models
from oauth2_provider.models import Application


class DeviceType(models.Model):
    value = models.CharField(max_length=200)


class EquipmentModel(models.Model):
    device_type = models.OneToOneField(DeviceType, on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    version = models.CharField(max_length=200, null=True)
    cpu = models.CharField(max_length=200)
    cpu_cores = models.IntegerField()
    cpu_clock_mhz = models.IntegerField()
    flash_mb = models.CharField(max_length=200)
    ram_mb = models.IntegerField()
    ethernet_100MB_ports = models.IntegerField()
    ethernet_gbit_ports = models.IntegerField()
    wlan_hardware = models.CharField(max_length=255)
    wlan_24ghz = models.CharField(max_length=200)
    wlan_50ghz = models.CharField(max_length=200)
    bluetooth_support = models.CharField(max_length=200)
    usb_ports = models.CharField(max_length=200)
    serial = models.BooleanField(null=True)
    power_supply = models.CharField(max_length=200, null=True)


class Equipment(models.Model):
    model = models.ForeignKey(EquipmentModel, on_delete=models.SET_NULL, null=True)
    registery_date = models.DateTimeField(auto_now_add=True)
    community = models.ForeignKey('communities.Community', on_delete=models.CASCADE)
    owner = models.ForeignKey('users.ServiceProviderProfile', on_delete=models.CASCADE)
    picture = models.ImageField(blank=True, null=True)

class ApplicationProfile(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    owner = models.ForeignKey('users.ServiceProviderProfile', on_delete=models.CASCADE, default='')
    picture = models.ImageField(blank=True, null=True)