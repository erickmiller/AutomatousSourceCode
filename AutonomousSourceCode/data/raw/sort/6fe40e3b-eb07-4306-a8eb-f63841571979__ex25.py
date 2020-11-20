def break_words(stuff):
	"""This function will break up words for us"""
	words = stuff.split(' ') # split stuff
	return words

def sort_words(words):
	"""Sorts the words"""
	return sorted(words) #sort words

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)  # pop the first word
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1) # pop the last word
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words"""
	words = break_words(sentence) #split sentence
	return sort_words(words) #sort words

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence"""
	words = break_words(sentence) #split sentence
	print_first_word(words) # print the first word
	print_last_word(words) # print the last word

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence) # sort sentence
	print_first_word(words) #print the first word
	print_last_word(words) #print the last word

sentence = "All good things come to those who wait."
words = break_words(sentence)
print words
	
sorted_words = sort_words(words)
print sorted_words

print_first_word(words)

print_last_word(words)

print words
	
print_first_word(sorted_words)
print_last_word(sorted_words)

print sorted_words

sorted_words = sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)