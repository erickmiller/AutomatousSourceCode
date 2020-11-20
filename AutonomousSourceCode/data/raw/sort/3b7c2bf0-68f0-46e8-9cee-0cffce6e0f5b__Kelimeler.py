def breakWords(sentence):
    words = sentence.split(' ')
    return words

def getLastWord(sentence):
    wordList = breakWords(sentence)
    word = wordList.pop(-1)
    return word

def getFirstWord(sentence):
    wordList = breakWords(sentence)
    word = wordList.pop(0)
    return word

def sortWords(words):
    return sorted(words)

def sortSentence(sentence):
    wordList = breakWords(sentence)
    return sortWords(wordList)

