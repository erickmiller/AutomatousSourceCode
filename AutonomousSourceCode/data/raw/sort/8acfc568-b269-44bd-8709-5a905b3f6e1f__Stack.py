class Stack:
 def __init__(self):
  self.elements = []

 def pop(self):
  return self.elements.pop()

 def push(self, x):
  self.elements.append(x)

 def isEmpty(self):
  return self.elements == []

 def peek(self):
  return self.elements[-1]

def sort(a):
 if a.isEmpty():
  return a
 b = Stack()
 sorted = False
 while not sorted:
  sorted = True
  while not a.isEmpty():
   x = a.pop()
   if a.isEmpty():
    b.push(x)
    continue
   if x > a.peek():
    sorted = False
    b.push(a.pop())
    a.push(x)
   else:
    b.push(x)
  while not b.isEmpty():
   a.push(b.pop())
 return a

a = Stack()
a.push(3)
a.push(1)
a.push(4)
a.push(2)
a = sort(a)
while not a.isEmpty():
 print a.pop()

