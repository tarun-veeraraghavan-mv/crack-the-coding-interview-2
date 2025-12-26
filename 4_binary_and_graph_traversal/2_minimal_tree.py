"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algo-
rithm to create a binary search tree with minimal height.
"""

# The logic is to make the middle element in the arr input as the root and then 
# get the left and right will be built recursively

from defenition_bst import Node

arr = [1,2,3,4,5]

def minimal_tree(my_arr: list[int]):
    if not my_arr:
        return None
    
    mid = len(my_arr) // 2

    val = my_arr[mid]

    root = Node(val=val)

    root.left = minimal_tree(my_arr=my_arr[0:mid])
    root.right = minimal_tree(my_arr=my_arr[mid+1:])

    return root

root = minimal_tree(my_arr=arr)

print("Printing the minimal tree:")
queue = [root]

while len(queue) > 0:
    root = queue.pop(0)

    print(root.val)

    if root.left:
        queue.append(root.left)
    if root.right:
        queue.append(root.right)