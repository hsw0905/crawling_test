from django.conf.urls import url
from django.urls import include
from rest_framework.routers import SimpleRouter

from zones.views import CarZoneViewSet

router = SimpleRouter(trailing_slash=False)

router.register(r'CarZone', CarZoneViewSet)

urlpatterns = [
    url('', include(router.urls)),
]