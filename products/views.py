from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    SAFE_METHODS,
    IsAuthenticatedOrReadOnly,
)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer
from users.permissions import IsAdminUser
from .pagination import ProductPagination
from .filters import ProductFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    pagination_class = ProductPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter

    search_fields = ["title", "description", "slug", "tags"]

    lookup_field = "id"

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAuthenticated(), IsAdminUser()]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAuthenticated(), IsAdminUser()]
