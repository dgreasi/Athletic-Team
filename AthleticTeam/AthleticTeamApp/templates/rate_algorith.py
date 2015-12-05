from django import template

register = template.Library()

@register.filter
def algorithm(value, args):
    temp = value + args(0)

    temp = temp / 2
    return temp