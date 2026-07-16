import json
from django.core.management.base import BaseCommand
from products.models import Product, ProductImage


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        with open("seed/seed.json", encoding="utf-8") as file:
            data = json.load(file)

        for item in data["products"]:
            product = Product.objects.create(
                title=item["title"],
                description=item["description"],
                slug=item["slug"],
                price=item["price"],
                stock=item["stock"],
                gender=item["gender"],
                sizes=item["sizes"],
                clothe_type=item["clothe_type"],
                tags=item["tags"],
            )

            for image in item["images"]:
                ProductImage.objects.create(product=product, image=f"products/{image}")

        self.stdout.write("Productos importados")
