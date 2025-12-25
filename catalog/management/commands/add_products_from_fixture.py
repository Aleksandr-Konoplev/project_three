from django.core.management.base import BaseCommand
from catalog.models import Category, Product
import json


class Command(BaseCommand):
    help = "Добавление продуктов и категорий в БД из JSON-фикстуры"

    def add_arguments(self, parser):
        parser.add_argument(
            "fixture_path", type=str, help="Путь к JSON-файлу с фикстурой"
        )

    def handle(self, *args, **options):
        fixture_path = options["fixture_path"]

        with open(fixture_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        categories_cache = {}

        for item in data:
            if item["model"] == "catalog.category":
                fields = item["fields"]
                category, created = Category.objects.get_or_create(
                    name=fields["name"],
                    defaults={"description": fields.get("description", "")},
                )
                categories_cache[item["pk"]] = category

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'Категория "{category.name}" добавлена')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f'Категория "{category.name}" уже существует'
                        )
                    )

        for item in data:
            if item["model"] == "catalog.product":
                fields = item["fields"]
                category_pk = fields["category"]
                category = categories_cache.get(category_pk)

                product_data = {
                    "category": category,
                    "name": fields["name"],
                    "description": fields.get("description", ""),
                    "price": fields["price"],
                    "image": fields.get("image", ""),
                }

                product, created = Product.objects.get_or_create(**product_data)

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'Товар "{product.name}" добавлен')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Товар "{product.name}" уже существует')
                    )
