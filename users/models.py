from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




class CustomUser(AbstractUser):
    address = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200, blank=False)
    state = models.CharField(max_length=200, blank=False)
    zipcode = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=200, blank=False)
