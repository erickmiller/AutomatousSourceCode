#coding=utf-8

def break_words(stuff):
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    print "first word: ", word
    return word

def print_last_word(words):
    word = words.pop(-1)
    print "last word: ", word
    return word

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

aaa = "a. test string sdsd"
print_first_and_last(aaa)
print_first_and_last_sorted(aaa)
