from rest_framework import serializers

from products.models import Product, ProductImage
from users.serializers import UserSerializer


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = (
            "id",
            "image",
        )

    def get_image(self, obj):
        return obj.image.name.split("/")[-1]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "clothe_type",
            "images",
            "price",
            "stock",
            "gender",
            "sizes",
            "tags",
            "created_at",
            "updated_at",
            "created_by",
        )
        read_only_fields = (
            "slug",
            "created_at",
            "updated_at",
        )
