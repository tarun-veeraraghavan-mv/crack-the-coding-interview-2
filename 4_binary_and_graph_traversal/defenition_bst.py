# Binary Search tree notes

class Node():
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

tree = Node(val=1)
a = Node(val=2)
b = Node(val=3)
c = Node(val=4)
d = Node(val=5)
e = Node(val=6)
f = Node(val=7)

tree.left = a
tree.right = b

a.left = c
a.right = d

b.left = e
b.right = f

"""
        1
     2     3
   4   5  6  7
"""

# DFS types

## Preorder traversal 
## Visit the current node before its child nodes
# Pre order -> Print first
# Root - Left - Right
print("Preorder traversal")
def preorder_traversal(tree: Node):
    if tree != None:
        print(tree.val)
        preorder_traversal(tree=tree.left)
        preorder_traversal(tree=tree.right)

preorder_traversal(tree=tree)

## Inorder traversal
## Visit the left branch, the current node and then the right node
# In order -> Print middle
# Gets us the node values in ascending order
# Left - Root - Right
print("Inorder traversal")
def inorder_traversal(tree: Node):
    if tree != None:
        inorder_traversal(tree=tree.left)
        print(tree.val)
        inorder_traversal(tree=tree.right)

inorder_traversal(tree=tree)

## PostOrder Traversal
## Visits the current node after its children nodes
# Post order -> Print last
# Left - Right - Root
print("Postorder traversal")
def postorder_traversal(tree: Node):
    if tree != None:
      postorder_traversal(tree=tree.left)
      postorder_traversal(tree=tree.right)
      print(tree.val)
postorder_traversal(tree=tree)

# BFS
from collections import deque

def bfs(tree: Node):
    if not tree:
        return
    
    queue = [tree]

    while queue:
        current = queue.pop(0)
        print(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
          
print("BFS")
bfs(tree=tree)