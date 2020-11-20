#more practise

def break_words(stuff):
    """This function will break up words for us"""
    return stuff.split(' ')

def sort_words(words):
    """Sort the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off"""
    print words.pop(0)

def print_last_word(words):
    """Prints the last word after popping it off"""
    print words.pop(-1)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the 1st and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one"""
    sorted_words = sort_sentence(sentence)
    print_first_word(sorted_words)
    print_last_word(sorted_words)
