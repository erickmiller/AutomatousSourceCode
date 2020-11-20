__author__ = 'kud'
def break_words(stuff):
    words = stuff.split(" ")
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    return word

def print_last_word(words):
    word = words.pop(-1)
    return word

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    return print_first_word(words) +"\n"+ print_last_word(words)


def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    return print_first_word(words) + "\n" + print_last_word(words)


s = "This is test sentence."

w = break_words(s)
sorted_words = sort_words(w)
print w
print sorted_words
print print_first_word(w)
print print_last_word(w)
print sort_sentence(s)
print print_first_and_last(s)
print print_first_and_last_sorted(s)
