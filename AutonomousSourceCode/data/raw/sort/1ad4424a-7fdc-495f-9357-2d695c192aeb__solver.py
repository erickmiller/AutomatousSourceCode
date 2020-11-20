import json;
import os.path

def sortLetters(word):
	return ''.join(sorted(word))

def firstLetters(word):
	currFirstThreeLetters = sortedWord[: min(3,len(word))]
	return currFirstThreeLetters

def solve(scrambledWord):
	sortedWord = sortLetters(scrambledWord)
	firstThree = firstLetters(sortedWord)
	filePath = "./processed_scrambles/" + firstLetters + ".json"

	if os.path.isfile(filePath):
		with open(filePath, "r") as infile:
			solutionsDict = json.loads(infile.read())
			if sortedWord in solutionsDict:
				return solutionsDict[sortedWord]
			else:
				return "NOT IN FILE"
	else:
		return "FILE DOES NOT EXIST"

import sys

for line in sys.stdin:
    print line
    solve(line)