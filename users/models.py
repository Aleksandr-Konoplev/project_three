from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


class User(AbstractUser):
    username = None
    email = models.CharField(verbose_name="Email", unique=True)

    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите изображение",
    )
    phone = models.CharField(
        verbose_name="Номер телефона",
        max_length=25,
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    country = CountryField(blank=True, null=True)
    token = models.CharField(
        max_length=100, verbose_name="Token", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
