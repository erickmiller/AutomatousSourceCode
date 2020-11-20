from django import template

register = template.Library()

@register.filter
def sort(values, arg):
    if arg:
        return sorted(values)
    else:
        return values
