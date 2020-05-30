from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

class AddressData(models.Model):
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=250)


class CustomUser(AbstractUser):
    address = models.ForeignKey(AddressData, related_name='user', on_delete=models.CASCADE, blank=True, null=True)
