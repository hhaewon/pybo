from django import template

register = template.Library()


@register.filter()
def sub(value: int, arg: int):
    return value - arg
