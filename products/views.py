from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer
from users.permissions import IsStoreUser, IsAdminUser, IsSuperUser

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated(), IsStoreUser()]
        return [IsAuthenticated(), IsAdminUser()]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated(), IsStoreUser()]
        return [IsAuthenticated(), IsAdminUser()]