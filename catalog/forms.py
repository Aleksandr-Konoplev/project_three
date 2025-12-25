from django import forms
from .models import Product, Category
from django.core.exceptions import ValidationError


class CategoryForm(forms.ModelForm):
    pass


class ProductForm(forms.ModelForm):
    pass