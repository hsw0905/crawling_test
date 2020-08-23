from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from zones.models import CarZone
from zones.serializers import CarZoneSerializer


class CarZoneViewSet(ModelViewSet):
    queryset = CarZone.objects.all()
    serializer_class = CarZoneSerializer
