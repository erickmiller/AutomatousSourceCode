# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
    	if not head or not head.next:
    		return head
    	sortedHead = None
    	p = head
    	sortedTail = None
    	while p:
    		next = p.next
    		if not sortedHead or p.val < sortedHead.val:
    			p.next = sortedHead
    			sortedHead = p
    			if not sortedTail:
    				sortedTail = sortedHead
    		elif sortedTail and sortedTail.val < p.val:
    			sortedTail.next = p
    			p.next = None
    			sortedTail = sortedTail.next
    		else:
    			q = sortedHead
    			while q.next and q.next.val <= p.val:
    				q = q.next
    			p.next = q.next
    			q.next = p
    		p = next
    	return sortedHead


     #    if head is None:
     # 	      return head
     #    before = None
     #    toSort = head
     #    next = toSort.next
     #    while toSort:
     #    	p = head
     #    	last = None
     #    	while p and p != toSort: #and p != next:
     #    		if p.val > toSort.val:
     #    			if last:
     #    				last.next = toSort
     #    			else:
     #    				head = toSort
     #    			if before:
     #    				before.next = None
     #    			toSort.next = p
     #    			break
     #    		last = p
     #    		p = p.next
     #    	if not p:
     #    		before.next = toSort
     #    		before = toSort
     #    		toSort.next = None
     #    	if p == toSort:
     #    		before = toSort
     #    	toSort = next
     #    	if next:
     #    	   	next = next.next

     #    	# h = head
     #    	# while h:
     #    	# 	print h.val,
     #    	# 	h = h.next
     #    	# print 
     #    return head

s = Solution()
h = None
tail = None
for i in [3,4,1] * 1:
	if not h:
		h = ListNode(i)
		tail = h
	else:
		tail.next = ListNode(i)
		tail = tail.next
h = s.insertionSortList(h)
while h:
	print h.val,
	h = h.next







