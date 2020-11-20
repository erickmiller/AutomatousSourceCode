from collections import Counter

def mysucc(number):
    return number + 1

def mymax(a, b):
    return a if a > b else b

def countWords(string):
    if string.strip() == "":
        return 0
    words = string.strip().split(' ')
    return len(words)

def countWords2(string):
    if string.strip() == "":
        return 0
    words = string.strip().split(' ')
    c = Counter(words)
    for word in sorted(c.keys()):
        print(word, c[word])

def orderWords(words):
    c = Counter(words)
    s = sorted(c.keys()) #sort lexically
    return sorted(s, key=c.get,reverse=True)

def shorten(string,n):
    c = Counter([a for a in string if a.isalpha()])
    top =  sorted(sorted(c.keys()), key=c.get,reverse=True)[:n]
    return "".join([a for a in string if not a in top])
