# Merge sort has 2 functions: break and merge. 
# Break will split the input list into halves and the merge function will merge 2 sorted lists together


def merge(list1: list[int], list2: list[int]):
    combined = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])

    while j < len(list2):
        combined.append(list2[j])

    return combined

def merge_sort(my_list: list[int]):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[0:mid_index]) 
    right = merge_sort(my_list[mid_index:]) 

    return merge(left, right)

print(merge_sort([4,3,6,1,2]))