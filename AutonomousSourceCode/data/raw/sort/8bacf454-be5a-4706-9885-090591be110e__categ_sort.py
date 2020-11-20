from django import template
from catalog.additions import SORTED_PRODUCT_OPTION
register = template.Library()

@register.inclusion_tag('templatetags/categ_sort.html')
def categ_sort(selected):
    return {
        'sorted_options': SORTED_PRODUCT_OPTION,
        'selected': selected
    }
