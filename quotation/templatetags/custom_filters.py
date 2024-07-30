from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def mul(value, arg):
    return round(value * Decimal(arg)+value,2)