"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. Ifxis contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""

from linked_list import Node, head

def partition(head: Node, partition: int):
    small_head = Node(val=0)
    big_head = Node(val=0)
    small_tail = small_head
    big_tail = big_head

    curr = head

    # fill up the 2 lists
    while curr:
        if curr.val < partition:
            small_tail.next = curr
            small_tail = curr
        else:
            big_tail.next = curr
            big_tail = curr

        curr = curr.next

    # link 2 of the lists together
    small_tail.next = big_head.next
    big_tail.next = None
    
    # clean up
    new_head = small_head.next
    small_head.next = None

    big_head.next = None

    return new_head