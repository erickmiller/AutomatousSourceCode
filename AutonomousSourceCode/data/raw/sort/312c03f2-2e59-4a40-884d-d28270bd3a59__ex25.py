# Defining different types of functions

def break_words(stuff):
	"""This is a sample help statement"""
	words = stuff.split(' ')
	return words

def sort_words(words):
	return sorted(words)

def print_first_word(words):
	word = words.pop(0)
	print word

def print_last_word(words):
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)
