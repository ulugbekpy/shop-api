from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from .views import ProductViewSet, CollectionViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("collections", CollectionViewSet)

urlpatterns = router.urls
