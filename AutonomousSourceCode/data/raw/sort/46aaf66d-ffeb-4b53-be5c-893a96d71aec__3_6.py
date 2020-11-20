from stack import Stack

def sort_stack(my_stack):
    # Case input empty stack
    if my_stack.is_empty():
        return []

    # Case input stack is one element long
    sorted_stack = Stack()
    sorted_stack.push(my_stack.pop())
    if my_stack.is_empty():
        return sorted_stack

    # General case
    while not my_stack.is_empty():
        temp = my_stack.pop()
        if temp <= sorted_stack.peek():
            sorted_stack.push(temp)
        else:
            popped = 0
            while not (sorted_stack.is_empty() or temp < sorted_stack.peek()):
                my_stack.push(sorted_stack.pop())
                popped += 1
            sorted_stack.push(temp)
            while popped > 0:
                sorted_stack.push(my_stack.pop())
                popped -= 1

    return sorted_stack # return a stack in descending order


my_stack = Stack( [3,4,5,2,1,9] )
my_sorted =  sort_stack(my_stack)
print my_sorted
print my_sorted.pop()
print my_sorted
