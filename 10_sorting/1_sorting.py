"""
Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
"""

a = [1,3,5,7,0,0,0]
b = [2,4,6]

def sorted_merge(a: list[int], b: list[int]):
    i = 3
    j = 2
    back = 6

    while a[i] > b[j]:
        a[back] = a[i]
        i -= 1
        back -= 1

    while a[i] < b[j]:
        a[back] = b[j]
        j -= 1
        back -= 1

    