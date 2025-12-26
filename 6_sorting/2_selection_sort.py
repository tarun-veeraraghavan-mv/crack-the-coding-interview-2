# Selection sort
# Time complexity: O(n^2)

my_list = [5,4,1,6,2]

def selection_sort(my_list: list[int]):
    n = len(my_list)

    # i should not go to the end of the list
    for i in range(n-1):
        min_index = i
        # j will be one ahead of i and go to the end of the list
        for j in range(i+1, n):
            if my_list[j] < my_list[min_index]:
                min_index = j

        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

    return my_list

# print(selection_sort(my_list=my_list))
