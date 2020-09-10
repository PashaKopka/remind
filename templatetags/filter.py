from django import template

register = template.Library()


@register.filter(name='split')
def split(value, key):
    return value.split(key)


@register.simple_tag
def update_variable(value):
    """Allows to update existing variable in template"""
    return value + 1
