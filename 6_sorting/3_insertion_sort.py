# Time complexity: O(n^2)

my_list = [5,4,1,2,7]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        # While the current item is smaller than its left neighbor
        while j > 0 and arr[j] < arr[j - 1]:
            # Swap them immediately
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

# Example
print(insertion_sort([5, 4, 1, 2, 7]))