my_list = [5,4,1,2,7]

def insertion_sort(my_list: list[int]):
    for i in range(1, len(my_list)):
        j = i - 1
        while  j >= 0 and my_list[i] < my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]
            j -= 1

    return my_list

# print(insertion_sort(my_list=my_list))

arr = [1,2,3,4]

arr[0], arr[1] = arr[1], arr[0]

print(arr)