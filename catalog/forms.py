from django import forms
from .models import Product, Category
from django.core.exceptions import ValidationError
from catalog.constants import FORBIDDEN_WORDS


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description',)

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите название категории'
            }
        )

        self.fields['description'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите описание категории'
            }
        )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'category')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите название продукта'
            }
        )

        self.fields['description'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите описание продукта'
            }
        )

        self.fields['image'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )

        self.fields['price'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Введите цену продукта'
            }
        )

        self.fields['category'].queryset = Category.objects.all()

    def clean_name(self):
        """ Проверка на существование добавляемого продукта,
        или не входит ли добавляемое название в список запрещенных """
        name = self.cleaned_data.get('name')

        #Проверка на существование товара
        qs = Product.objects.filter(name=name)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise ValidationError('Такой товар уже существует')

        # Проверка на наличие запрещенных слов
        forbidden_words_list = FORBIDDEN_WORDS.split()
        for word in forbidden_words_list:
            if word in name.lower():
                raise ValidationError(f'В названии товара есть слово "{word}" входящее в список запрещенных')
        return name

    def clean_price(self):
        """ Проверка цены (не может быть отрицательной) """
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Цена должна быть положительным числом')
        return price

