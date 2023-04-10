import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def sub(value: int, arg: int):
    return value - arg


@register.filter()
def mark(value: str):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))
