from django.db import models


# Create your models here.
class CarZone(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=255)
    region = models.CharField(max_length=20, default='seoul')
    detail = models.CharField(max_length=255, default='')
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
