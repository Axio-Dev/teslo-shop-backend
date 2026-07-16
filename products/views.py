from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer
from users.permissions import IsStoreUser, IsAdminUser, IsSuperUser

class ProductViewSet(ModelViewSet):
    permission_classes = [IsStoreUser, IsAdminUser, IsSuperUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"

class ProductImageViewSet(ModelViewSet):
    permission_classes = [IsAdminUser, IsSuperUser]
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer