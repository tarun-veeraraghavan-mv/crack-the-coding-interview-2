"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
Hints: #8, #25, #41, #67, #126
"""

from linked_list import head, Node

def kth_to_last1(head: Node, k: int):
    slow, fast = head, head

    for _ in range(k):
        fast = fast.next

    while fast and fast.next:
        fast = fast.next
        slow = slow.next

    return slow.val

def kth_to_last2(k: int):
    length = 0
    dummy = head
    while dummy:
        length += 1
        dummy = dummy.next

    to_find_index = length - 1 - k

    dummy2 = head
    for i in range(to_find_index):
        dummy2 = dummy2.next

    return dummy2.val

print(kth_to_last1(head=head, k=2))
print(kth_to_last1(head=head, k=3))

print(kth_to_last2(k=2))
print(kth_to_last2(k=3))