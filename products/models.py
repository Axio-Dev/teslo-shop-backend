import uuid

from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class Product(models.Model):

    class Gender(models.TextChoices):
        MEN = "men", "Men"
        WOMEN = "women", "Women"
        KID = "kid", "Kid"
        UNISEX = "unisex", "Unisex"

    class Sizes(models.TextChoices):
        XS = "xs", "XS"
        S = "s", "S"
        M = "m", "M"
        L = "l", "L"
        XL = "xl", "XL"
        XXL = "xxl", "XXL"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, db_index=True)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=20, choices=Gender.choices)
    sizes = ArrayField(models.CharField(max_length=5, choices=Sizes.choices), default=list, blank=True)
    tags = ArrayField(models.CharField(max_length=50), default=list, blank=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.image.name