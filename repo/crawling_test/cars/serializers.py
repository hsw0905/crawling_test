from rest_framework.serializers import ModelSerializer

from cars.models import Car


class CarSerializer(ModelSerializer):
    class Meta:
        model = 'cars.Car'
        fields = ['id',
                  'number',
                  'name',
                  'zone',
                  'manufacturer',
                  'fuel',
                  'type',
                  'shift_type',
                  'is_event_model',
                  'manual_page',
                  'safety_option',
                  'convenience_option'
                  ]
        read_only_fields = ['id',
                            'number',
                            'name',
                            'zone',
                            'manufacturer',
                            'fuel',
                            'type',
                            'shift_type',
                            'is_event_model',
                            'manual_page',
                            'safety_option',
                            'convenience_option'
                            ]
