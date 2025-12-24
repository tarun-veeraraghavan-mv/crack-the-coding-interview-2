"""
Palindrome: Implement a function to check if a linked list is a palindrome.
Hints: #5, #13, #29, #61, #101
"""

from linked_list import Node, head

def palindrome_ll(head: Node):
    slow = fast = head

    # find the middle of the ll
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # reverse the second half of the list from the slow node
    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # check both the halves
    left = head
    right = prev

    while left and right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True

print(palindrome_ll(head=head))