from time import sleep
from threading import Thread

class SleepSort:
	def __init__(self, to_sort):
		self.list_to_sort = to_sort
		self.sorted_items = []

	def sleep_sort(self, arg):
		sleep(arg)
		self.sorted_items.append(arg)
	def sort(self):
		threads = []
		for i in self.list_to_sort:
			t = Thread(target=self.sleep_sort, args=(i,))
			t.start()
			threads.append(t)
		for a in threads:
			a.join()
		return list(self.sorted_items)
sort = SleepSort([1, 4, 3, 9, 11, 2])
print(sort.sort())