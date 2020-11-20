def break_w(words) : 
	return words.split(' ')
	
def get_first(words) : 
	return words.pop(0)
	
def get_last(words) : 
	return words.pop(-1)
	
def sort(words) : 
	"""Sorts the words"""
	return sorted(words)
	
def sort_sentence(words) :
	"""sorts sentence"""
	break_words = break_w(words)
	return sort(break_words)
	
def print_first_last(sentence) :
	"""prints first and last word from sorted sentence"""
	sw = sort_sentence(sentence)
	print get_first(sw), get_last(sw)
	
	
print_first_last("ovo je proba i testiram nesto")
	