from rest_framework import serializers

from products.models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Product
        fields = (
            "title",
            "slug",
            "description",
            "images",
            "price",
            "stock",
            "gender",
            "sizes",
            "tags",
            "user",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "slug",
            "created_at",
            "updated_at",
        )            