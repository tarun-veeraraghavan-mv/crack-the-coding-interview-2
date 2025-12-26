"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""

from defenition_bst import Node, tree
from linked_list import Node as LinkedListNode

def list_of_depths(root: Node) -> LinkedListNode:
    output = LinkedListNode(val=0)
    tail = output

    queue = [root]

    while len(queue) > 0:
        curr = queue.pop(0)

        new_node = LinkedListNode(val=curr.val)

        tail.next = new_node
        tail = tail.next

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)

    return output.next

ll = list_of_depths(root=tree)

dummy = ll

print("Node values")
while dummy and dummy.next:
    print(dummy.val)
    dummy = dummy.next