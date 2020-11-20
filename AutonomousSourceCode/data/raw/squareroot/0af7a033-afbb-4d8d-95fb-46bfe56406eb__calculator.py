class Calculator(object):

	def __init__(self):
		self.result = 0
	
	def add(self, n):
		self.result = self.result + n

	def subtract(self, n):
		self.result = self.result - 1

	def multiply(self, n):
		pass

	def divide(self, n):
		self.result = self.result / n

	def square(self, n):
		self.result = n * n

	def squareRoot(self, n):
		while True:
			pass

	def clear(self):
		self.result = 0

	def switchOn(self):
		self.result = 0

	def switchOff(self):
		pass

	def getResult(self):
		return self.result
