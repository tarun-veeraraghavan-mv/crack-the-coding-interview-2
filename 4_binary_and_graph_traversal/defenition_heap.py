# Heap: [2,5,0,1,10,8,-4,3,12,9]
# if i is the current node, then the left is in 2i + 1 position and right node is in the 2i+2 position
# For i = 3 which is node with val 1, the left node is in 2*3+1 = 7 which is 3 and right node
# is in 2*3+2 = 12

# Heap has two types: Min heap and max heap
# Min heap is where the children node's value is always bigger than the parent's node. Meaning small -> big
# Max heap is where the children node's value is always smaller than the parent's node. Meaning big -> small

# Heap pop for min heap will get the root as it is the least value (O(1))
# Heap pop for max heap will get the root as it is the greatest value (O(1))

# Heap push will take in a new value and arrange it correctly. It is O (log n)

# Heap sort: O (n * log(n))


# NOTE: heapq library always makes a min heap by default. To make a max heap you need to make some changes
# to the initial list structure
import heapq

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

heapq.heapify(A)

print(A)

heapq.heappush(A, 4)

print(A) # 4 is added

heapq.heappop(A)

print(A) # -4 is the least and it is removed

# Making a max heap

B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

n = len(B)

for i in range(n):
    B[i] = -B[i]

heapq.heapify(B)

print(B)

largest = -heapq.heappop(B)

print(largest)