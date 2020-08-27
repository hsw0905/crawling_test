from django.conf.urls import url
from django.urls import include
from rest_framework.routers import SimpleRouter

from cars.views import CarViewSet
from prices.views import CarPriceViewSet
from zones.views import CarZoneViewSet

router = SimpleRouter(trailing_slash=False)

router.register('CarZone', CarZoneViewSet)
router.register('Car', CarViewSet)
router.register('CarPrice', CarPriceViewSet)

urlpatterns = [
    url('', include(router.urls)),
]