from helper import *


def insert_sort(head):
    sorted_head = head
    if not head or not head.next:
        return sorted_head

    head = head.next
    if head.val < sorted_head.val:
        sorted_head.next = head.next
        head.next = sorted_head
        sorted_head, head = head, sorted_head

    while head:
        pre = sorted_head
        cur = sorted_head.next
        while cur and head.val >= cur.val:
            cur = cur.next
            pre = pre.next
        else:
            if not cur:
                break
            pre.next = cur.next
            cur.next = pre
        head = head.next
    return sorted_head


if __name__ == '__main__':
    head = build_llist([29, 23, 82, 11])
    print_llist(head)

    pro_head = insert_sort(head)
    print_llist(pro_head)
