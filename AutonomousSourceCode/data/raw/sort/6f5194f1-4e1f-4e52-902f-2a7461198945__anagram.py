# 10/10/15 from Cracking the Coding Interview

def anagram_method1(string1, string2):
    return histogram(string1) == histogram(string2)

def histogram(string):
    res = {}
    for letter in string:
        if letter in res:
            res[letter] = res[letter] + 1
        else:
            res[letter] = 1
    return res

def anagram_method2(string1, string2):
    return sort(string1) == sort(string2)

def sort(string):
    return ''.join(sorted(string))
