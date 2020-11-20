"""
Write a program to sort a stack in ascending order (with biggest item on top). You may use additional stacks to hold items, but you may not copy  the elements into
any other data structure (like array). The stack support the following operations push, pop, peek and is_empty.

"""


def sort_stack(stack):

    def peek(stack): return stack[-1]

    sorted_stack = []

    while stack:
        number = stack.pop()

        if stack and number > peek(stack):
            sorted_stack.append(number)
        else:
            while sorted_stack and peek(sorted_stack) > number:
                stack.append(sorted_stack.pop())

            sorted_stack.append(number)

    return sorted_stack


print(sort_stack([7, 73, 65, 23, 8, 77, 1, 24]))


def sort(A):
    # Sort stack without additional space
    # basically stack + recursion i.e more stacks. FUN
    def insert(A, num):
        if not A:
            A.append(num)
        else:
            if num < A[-1]:
                last_popped = A.pop()
                insert(A, num)
                insert(A, last_popped)
            else:
                A.append(num)

        return A

    if not A: return A

    num = A.pop()
    sort(A)
    insert(A, num)

    return A

# A = [4,5,3,1,2]
# A = [1,2,3,4,5]

A = [1,2,3,6,5,4]

print(sort(A))

