class BearSlowlySorts:
	def minMoves(self, w):
		if self.sorted(w):
			return 0
		w1 = list(w)
		w1 = self.sortFront(w1)
		if self.sorted(w1):
			return 1
		w2 = list(w)
		w2 = self.sortEnd(w2)
		if self.sorted(w2):
			return 1
			
		w1 = self.sortEnd(w1)
		if self.sorted(w1):
			return 2
		w2 = self.sortFront(w2)
		if self.sorted(w2):
			return 2
		return 3
	
	def sorted(self, w):
		prev = 0
		for v in w:
			if v < prev:
				return False
			prev = v
		return True
	
	def sortFront(self, w):
		front = list(w[:-1])
		front.sort()
		front.append(w[-1])
		return front
	
	def sortEnd(self, w):
		end = list(w[1:])
		end.sort()
		ret = [w[0]]
		ret += end
		return ret
