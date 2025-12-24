"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

from linked_list import head, Node

def remove_dups(head):
    i = head
    while i:
        j = i
        while j.next:
            if j.next.val == i.val:
                j.next = j.next.next
            else:
                j = j.next
        i = i.next

remove_dups(head=head)