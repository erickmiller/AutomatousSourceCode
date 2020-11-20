from django.utils.datastructures import SortedDict
from bencode import bencode, bdecode

def sort_dict(D):
	result = SortedDict()
	for key in sorted(D.keys()):
		if type(D[key]) is dict:
			D[key] = sort_dict(D[key])
		result[key] = D[key]
	return result