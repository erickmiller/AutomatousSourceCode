def breakWords(stuff):
	return stuff.split(' ')

def sortWords(words):
	return sorted(words)

def printFirstWord(words):
	print words.pop(0)

def printLastWord(words):
 	return words.pop(-1)

def sortSentence(sentence):
	return sortWords(breakWords(sentence))

def printFirstAndLast(sentence):
	words = breakWords(sentence)
	printFirstWord(words)
	printLastWord(words)

def printFirstAndLastSorted(sentence):
	words = sortSentence(sentence)
	printFirstWord(words)
	printLastWord(words)