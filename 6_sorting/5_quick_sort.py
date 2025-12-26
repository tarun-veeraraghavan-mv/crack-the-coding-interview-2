# Time complexity: O(n * log(n))
# Watch this video: https://www.youtube.com/watch?v=kFeXwkgnQ9U

def quick_sort(sequence: list[int]):
    # base case to end the recursion
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    # segregate the elements into greater and lower lists based on the pivot values
    items_greater = []
    items_smaller = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_smaller.append(item)

    # repeate the quick sort for the smaller item list and greater item list
    return quick_sort(items_smaller) + [pivot] + quick_sort(items_greater)