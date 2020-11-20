# Time: O(n^2)
# Space: O(n)
def stack_sort(stack):
    sorted_stack = []
    while stack:
        temp = stack.pop()
        while sorted_stack and sorted_stack[-1] > temp:
            stack.append(sorted_stack.pop())
        sorted_stack.append(temp)
    return sorted_stack

if __name__ == '__main__':
    stack = [3, 2, 4, 6, 3, 1, 5]
    print 'sorting stack:', stack
    print stack_sort(stack)
