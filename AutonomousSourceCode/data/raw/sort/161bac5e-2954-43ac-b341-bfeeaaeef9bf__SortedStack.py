# write a program to sort a stack in ascending order (with biggest item on top of the stack). You may use atmost one additional stack to hold items. 
# But you may not use any other data structure. The stack supports push, pop, peek, isEmpty
# Question Source: Cracking the coding interview by Gayle Laakmann Mcdowell

import Stack as stk

def sortTheStack(stack1): 
	if (stack1.isEmpty()):
		print "Stack is empty. Nothing to sort."
		return None
	sortedStack = stk.Stack() # This is the second stack that will always hold elements in sorted order (smallest element on top of the stack).
	while (not stack1.isEmpty()):
		count = 0
		temp = stack1.pop()
		if(sortedStack.isEmpty()):
			sortedStack.push(temp)
		else:			
			if(temp < sortedStack.peek()):
				sortedStack.push(temp)
			else:
				while ( (not sortedStack.isEmpty()) and (temp > sortedStack.peek()) ):
					stack1.push(sortedStack.pop())
					count = count + 1
				sortedStack.push(temp)
				for i in range(0,count):
					sortedStack.push(stack1.pop())
	while( not sortedStack.isEmpty()):
		stack1.push(sortedStack.pop())
	return 	stack1					

					


	





def main():
	unSortedStack = stk.Stack()
	unSortedStack.push(5)
	unSortedStack.push(3)
	unSortedStack.push(2)
	unSortedStack.push(4)
	unSortedStack.push(1)
	print "Before Sorting: "
	unSortedStack.printStack()
	sorted = sortTheStack(unSortedStack) 
	if (sorted != None):
		print "After Sorting: "
		sorted.printStack()


	


if __name__ == "__main__":
	main()	

