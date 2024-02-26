from django.urls import include, path
from rest_framework import routers
from .views import CrudViewSet

router = routers.DefaultRouter()
router.register(r'posts', CrudViewSet, basename="crud")

urlpatterns = [
    path('', include(router.urls)),
]