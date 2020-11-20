def break_words(stuff):
	""" Blah blah blah"""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"Sort sort Sort"
	return sorted(words)

def print_first_word(words):
	""" First First First"""
	word = words.pop(0)
	print word

def print_last_word(words):
	""" Last Last Last"""
	word = words.pop(-1)
	print word

def sorted_sentence(sentence):
	"""Sorts the words in the sentence"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""First and Last of sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	""" a b c"""
	words = sorted_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

