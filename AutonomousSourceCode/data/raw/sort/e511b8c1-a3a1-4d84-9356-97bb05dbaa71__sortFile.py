from listQfile import ListQ

class Sort(ListQ): #Aerver metoder fran listQ-klassen
    def __init__(self, unsortedList):
        self.items = unsortedList
        self.sortedList = []
        self.magicSort()

    def __str__(self):
    	s = ''
    	for n in self.sortedList:
    		s = s + str(n) + ' '
    	return s

        
    def magicSort(self): #Metod som laegger till varannat element langst bak i kon och naestkommande till en "sorterad lista".
        while not self.isEmpty():
            self.put(self.get())
            self.sortedList.append(self.get())