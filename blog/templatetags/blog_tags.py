from django import template
from django.conf import settings

register = template.Library()


@register.filter(name="add_class")
def add_class(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name="media_filter")
def media_filter(file_field):
    """
    Возвращает полный URL к файлу через MEDIA_URL.
    Используется в шаблоне: {{ post.image|media_filter }}
    """
    if file_field:
        return settings.MEDIA_URL + str(file_field)
    return ""
