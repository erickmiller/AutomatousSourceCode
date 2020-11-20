
def break_words(text):
    words = text.split(' ')
    return words


def sort_words(words):
    sorted_words = sorted(words)
    return sorted_words


def print_first_word(words):
    word = words.pop(0)
    print word


def print_last_word(words):
    word = words.pop(-1)
    print word


def sort_sentence(sentence):
    words = break_words(sentence)
    sorted_words = sort_words(words)
    return sorted_words


def print_first_and_last_word_sentence(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_word_soted_sentence(sentence):
    words = break_words(sentence)
    sorted_words = sort_words(words)
    print_first_word(sorted_words)


    print_last_word(sorted_words)
