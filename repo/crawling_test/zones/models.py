from django.db import models


# Create your models here.
class CarZone(models.Model):
    address = models.CharField(max_length=255, unique=True)
    region = models.CharField(max_length=20, default='seoul')
    detail = models.CharField(max_length=255, default='')
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
