from random import Random

class BogoSort(object):
	def sort(self, list):
		while not self.isSorted(list):
			self.shuffle(list)
		return list
	
	def isSorted(self, list):
		return sorted(list) == list
		
	def shuffle(self, list):
		Random().shuffle(list)
		return list