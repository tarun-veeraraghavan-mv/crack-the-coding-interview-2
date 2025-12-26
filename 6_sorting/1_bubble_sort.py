# Sort this list: [4,2,6,5,1,3]
# Logic: Compare the first item in the list with the second item, if the first item is
# greater than the second we will switch their positions. And then compare the second to the third 
# and so on
# Time complexity: O(n^2)
my_list = [4,2,6,5,1,3]

def bubble_sort(my_list: list[int]):
    n = len(my_list)
    # Outer loop to go through all the elements
    for i in range(n):
        # Inner loop to compare 2 adjacent element, we put -1 to prevent Index error and '-i' for 
        # efficiency reason as every time the loop ends the largest number in the array is at the end
        print(f"Performing comparisons for: {my_list[i]}")
        for j in range(0, n - i - 1):
            # Compare adjacent elements, if j is greater then j + 1, swap them
            print(f"Comparing {my_list[j]} and {my_list[j+1]}")
            if my_list[j] > my_list[j+1]:
                print(f"Swapping places as {my_list[j]} is bigger than {my_list[j+1]} ")
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                print(">" + str(my_list))
                continue
            print(f"No changes needed as {my_list[j]} is smaller than {my_list[j+1]}")

    return my_list

print(bubble_sort(my_list=my_list))