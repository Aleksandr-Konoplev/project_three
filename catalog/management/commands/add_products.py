from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавление продуктов в БД"

    def handle(self, *args, **options):

        clothes, _ = Category.objects.get_or_create(
            name="Одежда", description="Категория одежды"
        )
        shoes, _ = Category.objects.get_or_create(
            name="Обувь", description="Категория обуви"
        )

        products = [
            {
                "category": clothes,
                "name": "Куртка",
                "description": "Тёплая куртка",
                "price": 3000.00,
            },
            {
                "category": clothes,
                "name": "Штаны",
                "description": "Модные штаны",
                "price": 3999.00,
            },
            {
                "category": shoes,
                "name": "Кроссовки",
                "description": "Белые кроссовки",
                "price": 4500.00,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Товар {product.name} успешно добавлен")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"При добавлении товара {product.name} что-то пошло не так"
                    )
                )
