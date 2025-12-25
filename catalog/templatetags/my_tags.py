from django import template

register = template.Library()


@register.filter()
def media_filter(image):
    if image:
        return image.url
    return ""
