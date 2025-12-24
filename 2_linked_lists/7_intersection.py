"""
Intersection; Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
secting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jt h node of the second
linked list, then they are intersecting.
"""

from linked_list import Node, a, e

def intersection(link1: Node, link2: Node):
    # find the length of the linked lists
    headA, headB = link1, link2
    
    lengthA = 0
    while headA:
        lengthA += 1
        headA = headA.next

    lengthB = 0
    while headB:
        lengthB += 1
        headB = headB.next

    # move the pointers
    headC, headD = link1, link2
    if lengthA > lengthB:
        length_to_move = lengthA - lengthB
        while length_to_move > 0:
            headC = headC.next
            length_to_move -= 1
    if lengthA < lengthB:
        length_to_move = lengthB - lengthA
        while length_to_move > 0:
            headD = headD.next
            length_to_move -= 1

    # move till we find the common link
    while headC and headD:
        if headC == headD:
            return headC.val
        else:
            headC = headC.next
            headD = headD.next

print(intersection(link1=a, link2=e))