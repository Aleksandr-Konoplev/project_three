from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование категории', help_text='Введите категорию')
    description = models.TextField(verbose_name='Описание категории', help_text='Введите категорию')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=150, verbose_name='Наименование продукта', help_text='Введите наименование')
    description = models.TextField(verbose_name='Описание продукта', help_text='Введите Описание')
    image = models.ImageField(upload_to='products/',blank=True, null=True, verbose_name='Изображение продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена продукта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания продукта')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования продукта')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
