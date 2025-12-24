"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A->8->C->D->E- > C [the same C as earlier]
Output: C
"""

from linked_list import Node, head, j

def loop_detection(ll: Node):
    slow, fast = ll, ll

    # find the node where both fast and slow meet
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    # put the fast at the start of the node and then keep moving them 
    # one step until they meet
    fast = ll
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow.val
        
print(loop_detection(ll=j))