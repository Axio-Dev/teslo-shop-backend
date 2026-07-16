from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductImageViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(r"products-images", ProductImageViewSet, basename="products-images")

urlpatterns = [
    path("api/", include(router.urls)),
]
