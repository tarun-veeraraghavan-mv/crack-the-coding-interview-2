"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""

from defenition_bst import Node, tree
from linked_list import Node as LinkedListNode

def list_of_depths(root: Node) -> LinkedListNode:
    queue = [root]

    output_list = []

    while len(queue) > 0:
        output_node = LinkedListNode(val=0)

        tail = output_node

        for i in range(len(queue)):
            root = queue.pop(0)

            tail.next = LinkedListNode(val=root.val)

            tail = tail.next

            if root.left:
                queue.append(root.left)

            if root.right:
                queue.append(root.right)

        output_list.append(output_node.next)

    return output_list

output = list_of_depths(root=tree)

print("Print List")
for i in range(len(output)):
    print(f"At depth: {i}")
    lls: LinkedListNode = output[i]

    while lls:
        print(lls.val)
        lls = lls.next