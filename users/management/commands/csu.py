from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Создание суперпользователя с почтй: admin@mail.ru'

    def handle(self, *args, **options):
        email = 'admin@mail.ru'

        User.objects.filter(email=email).delete()

        user = User.objects.create(
            email=email,
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )
        user.set_password('1234qwer')
        user.save()

        self.stdout.write(
            self.style.SUCCESS(f'Пользователь {email} успешно создан')
        )
