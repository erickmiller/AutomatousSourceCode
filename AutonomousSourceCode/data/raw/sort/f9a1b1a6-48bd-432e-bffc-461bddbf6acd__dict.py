from django import template
register = template.Library()

@register.filter
def hash(h, key):
    return h[key]

@register.filter
def sort_hash(h, key):
    return sorted(h[key], key=lambda x: x.lower())
