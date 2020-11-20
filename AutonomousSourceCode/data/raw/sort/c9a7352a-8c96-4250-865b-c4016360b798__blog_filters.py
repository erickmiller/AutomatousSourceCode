from django import template
register = template.Library()

@register.filter(name='sort_dict')
def sort_dict(iterable):
	sorted_dict = {}
	sorted_keys = iterable.keys()
	sorted_keys.sort()

	for key in sorted_keys:
		sorted_dict[key] = iterable[key]

	return sorted_dict

