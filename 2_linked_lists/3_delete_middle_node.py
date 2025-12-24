"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
Input: the node c from the linked list a - >b- >c - >d - >e- >f
Result: nothing is returned, but the new linked list looks like a->b->d->e-> f
"""

from linked_list import head, Node

def delete_node(node: Node):
    if not node or node.next is None:
        return False

    next_node = node.next
    node.val = next_node.val
    node.next = next_node.next
    return True