"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the Vs digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7- > 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295,
Output:9 -> 1 -> 2,Thatis,912.
"""

# Question has so many edge cases like... 

from linked_list import Node, head

def sum_lists(link1: Node, link2: Node):
    dummy1 = link1
    dummy2 = link2
    carry = 0
    output_node = Node(val=0)
    current = output_node

    while dummy1 or dummy2 or carry:
        val1 = dummy1.val if dummy1 else 0
        val2 = dummy2.val if dummy2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        val = total % 10

        current.next = Node(val=val)
        current = current.next

        if dummy1:
            dummy1 = dummy1.next
        if dummy2:
            dummy2 = dummy2.next

    return output_node.next

