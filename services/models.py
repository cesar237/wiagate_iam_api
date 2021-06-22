from django.db import models
from oauth2_provider.models import Application


class DeviceType(models.Model):
    value = models.CharField(max_length=200)


class EquipmentModel(models.Model):
    device_type = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    version = models.CharField(max_length=200, null=True)
    cpu = models.CharField(max_length=200)
    cpu_cores = models.CharField(max_length=200)
    cpu_clock_mhz = models.CharField(max_length=200)
    flash_mb = models.CharField(max_length=200)
    ram_mb = models.CharField(max_length=200)
    ethernet_100MB_ports = models.CharField(max_length=200)
    ethernet_gbit_ports = models.CharField(max_length=200)
    wlan_24ghz = models.CharField(max_length=200)
    wlan_50ghz = models.CharField(max_length=200)
    bluetooth_support = models.CharField(max_length=200)
    usb_ports = models.CharField(max_length=200)
    serial = models.CharField(max_length=200, null=True)
    power_supply = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.brand


class Equipment(models.Model):
    model = models.ForeignKey(EquipmentModel, on_delete=models.SET_NULL, null=True)
    registery_date = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=200, null=True)
    community = models.ForeignKey('communities.Community', on_delete=models.CASCADE)
    owner = models.ForeignKey('users.ServiceProviderProfile', related_name='equipment_owner', on_delete=models.CASCADE)
    picture = models.ImageField(blank=True, null=True)

class ApplicationProfile(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    owner = models.ForeignKey('users.ServiceProviderProfile', related_name='application_owner', on_delete=models.CASCADE, default='')
    picture = models.ImageField(blank=True, null=True)