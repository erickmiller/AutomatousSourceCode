def break_words(stuff):
	''' doc comment duh ! '''
	return stuff.split()

def sort_words(words):
	return sorted(words)

def print_first_word(words):
	print words.pop(0)

def print_last_word(words):
	print words.pop(-1)

def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first(words)
	print_last(words)

def print_first_and_last_sorted(sentence):
	""" This is a pydoc comment """
	words = sort_sentence(sentence)
	print_first(words)
	print_last(words)
