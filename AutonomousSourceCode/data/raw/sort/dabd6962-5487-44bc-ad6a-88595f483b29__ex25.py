def break_words(stuff):
    """This function will break up words for us ."""
    #放在""" """"之间的内容就是这个函数的帮助文档，可以使用help（函数名）来查看
    words = stuff.split(' ')#str.split()按照给定分隔符分隔字符串
    return words

def sort_words(words):
    """Sort the word."""
    return sorted(words)#sorted()内建排序函数 list.sorted()

def print_first_word(words):
    """Prints the first word after poping it off."""
    word = words.pop(0)#list.pop(i)移除制定位置i的元素，并且返回该元素。参数为空时表示列表中最后一个元素
    print (word)

def print_last_word(words):
    """Print the last word after poping it off."""
    word = words.pop(-1)
    print (word)

def sort_sentence(sentence):
    """Take in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """print the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sort the words then prints the first and last one."""
    words=sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
