from rest_framework.serializers import ModelSerializer

from zones.models import CarZone


class CarZoneSerializer(ModelSerializer):
    class Meta:
        model = CarZone
