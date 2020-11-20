songs = open("songs.txt").readlines()

def sort(file):
	sortedList = []
	for i in range(len(file)):
		currentLowest = ord(file[0][0])
		for song in file[:i]:
			if ord(song[0]) < currentLowest:
				currentLowesst = ord(song[0])
				sortedList.append(song)
	return sortedList

