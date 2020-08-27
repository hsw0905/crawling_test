from rest_framework.serializers import ModelSerializer

from zones.models import CarZone


class CarZoneSerializer(ModelSerializer):
    class Meta:
        model = 'zones.CarZone'
        fields = ['id',
                  'zone_id',
                  'name',
                  'address',
                  'region',
                  'latitude',
                  'longitude',
                  'detail_info',
                  'blog_page']
        read_only_fields = ['id',
                            'zone_id',
                            'name',
                            'address',
                            'region',
                            'latitude',
                            'longitude',
                            'detail_info',
                            'blog_page']
