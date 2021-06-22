from django.db import models


class Community(models.Model):
    name = models.CharField(max_length=255)
    first_node = models.ForeignKey('services.Equipment', related_name='first_node', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    creator = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

