def binary_search(nums: list[int], num_to_find: int):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == num_to_find:
            # return the proper indexx
            return mid
        elif nums[mid] < num_to_find:
            left = mid + 1
        else:
            right = mid - 1

    return -1