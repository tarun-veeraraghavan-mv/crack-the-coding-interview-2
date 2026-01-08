# BASIC TEMPLATE
def backtrack_template(params):
    if base_case_condition:
        results.append(copy_of_solution)
        return
    
    for choice in choices:
        if violate_constraints:
            continue
        
        make_choice
        backtrack_template(updated_params)
        undo_choice


def subsets(nums: list[int]):
    result = []

    backtrack(0, nums=nums, result=result)

    return result

def backtrack(index, path, nums, result):
    # Base case to make a choice for every element
    if index == len(nums):
        # We must append a copy because path is modified later
        result.append(path[:])
        return
    
    # Decision 1: Include nums[index]
    path.append(nums[index])

    backtrack(index=index+1, path=path, nums=nums, result=result)

    # Backtrack: remove element to explore the skip branch
    path.pop()

    backtrack(index + 1, path, nums, result)