"""
generate a binary search tree
with minimum height
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs.binary_tree import Node


def array2bst(array):
    array.sort()

    def sort2bst(sorted):
        if not sorted:
            return None
        if len(sorted) == 1:
            return Node(sorted[0])
        if len(sorted) == 2:
            return Node(sorted[1], left=Node(sorted[0]))
        if len(sorted) > 2:
            mid = len(sorted) / 2
            root = Node(sorted[mid])
            left = sort2bst(sorted[:mid])
            right = sort2bst(sorted[mid + 1:])
            root.left = left
            root.right = right
            return root
    return sort2bst(array)


def main():
    root = array2bst([2, 4, 6, 22, 1, 42, 7, 8, 476, 23])

    def bfs(root):
        res = {}
        queue = []
        queue.append((root, 0))
        while queue:
            node, deep = queue.pop(0)
            print node.data,
            if node.left:
                queue.append((node.left, deep + 1))
            if node.right:
                queue.append((node.right, deep + 1))

    bfs(root)
    print ""
    for i in root.in_order():
        print i,
    print ""
    for i in root.pre_order():
        print i,

if __name__ == '__main__':
    main()
