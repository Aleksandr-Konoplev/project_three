from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Удаление всех категорий и продуктов из БД'

    def handle(self, *args, **options):

        # Удаляем все из бд
        num_del_prod, _ = Product.objects.all().delete()
        num_del_cat, _ = Category.objects.all().delete()

        if num_del_prod:
            self.stdout.write(self.style.SUCCESS(f'Удаленно {num_del_prod} продуктов'))
        else:
            self.stdout.write(self.style.WARNING('Продуктов для удаления не найдено'))

        if num_del_cat:
            self.stdout.write(self.style.SUCCESS(f'Удаленно {num_del_cat} категорий'))
        else:
            self.stdout.write(self.style.WARNING('Категорий для удаления не найдено'))
