# Sort a linked list using insertion sort.

# Hide Tags [Linked List] [Sort]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        lastSorted = head
        while lastSorted.next:
            if lastSorted.next.val < lastSorted.val:
                tmp = dummy
                while tmp.next.val < lastSorted.next.val:
                    tmp = tmp.next
                nextToSort = lastSorted.next
                lastSorted.next = nextToSort.next
                nextToSort.next = tmp.next
                tmp.next = nextToSort
            else:
                lastSorted = lastSorted.next
        return dummy.next