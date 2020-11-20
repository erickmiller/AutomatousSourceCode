__author__ = 'sereg'

def break_words(stuff):
    """This function will break words"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words"""
    return sorted(words)

def print_fw(words):
    word = words.pop(0)
    return word
def print_lw(words):
    word = words.pop(-1)
    print word
def sort_setnence(sentence):
    words = break_words(sentence)
    return sort_words(words)
def print_fwlw(sentence):
    words = break_words(sentence)
    print_fw(words)
    print_lw(words)

def print_fwlw_sort(sentence):
    words = sort_setnence(sentence)
    print_fw(words)
    print_lw(words)

sentence = "All good things come to those who wait"
print break_words(sentence)
print "-----------------------"
words = break_words(sentence)
print sort_words(words)
print "-----------------------"
print print_fw(words)
print "-----------------------"
print print_lw(words)
print "-----------------------"
sorted_words = sort_words(sentence)
print print_fw(sorted_words)
print "-----------------------"
print print_lw(sorted_words)
print "-----------------------"
sorted_words = sort_setnence(sentence)
print print_fwlw(sentence)
print "-----------------------"
print print_fwlw_sort(sentence)