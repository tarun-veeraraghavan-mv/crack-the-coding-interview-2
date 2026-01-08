# Fixed variable size pseudo code
def fixed_sliding_window(arr, k):
    # 1. Establish the initial state (the first window)
    window_result = initial_calculation(arr[:k])
    max_result = window_result
    
    # 2. Slide the window across the rest of the array
    for i in range(k, len(arr)):
        # What is coming in? -> arr[i]
        # What is going out? -> arr[i - k]
        
        # 3. Update the window result (O(1) operation)
        window_result = update_logic(window_result, arr[i], arr[i - k])
        
        # 4. Compare with the best result found so far
        max_result = max(max_result, window_result)
        
    return max_result

# Using this in the question with example
# Max Average Subarray
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # 1. First window: Sum the first k elements
        current_window_sum = sum(nums[:k])
        max_sum = current_window_sum
        
        # 2. Slide: Start from index k (the first element AFTER the first window)
        for i in range(k, len(nums)):
            # Update: Add the new guy (nums[i]), drop the old guy (nums[i-k])
            current_window_sum += nums[i] - nums[i - k]
            
            # Record: Keep the highest sum seen
            max_sum = max(max_sum, current_window_sum)
                
        # 3. Final Step: Convert the best sum to an average
        return max_sum / k
    
# Variable size sliding window
