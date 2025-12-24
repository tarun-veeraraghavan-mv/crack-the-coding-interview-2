"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
"""

stack: list[int] = [3,2,1,9,4]

def sort_stack(my_stack: list[int]):
    temp_stack = []

    print(f"Original stack: {stack}")
    print(f"Temp stack: {temp_stack}")

    while stack:
        # get the current pick from the original
        curr_pick = stack.pop()
        print(f"Current pick from the stack: {curr_pick}")
        # if the temp stack is empty or the topmost value in the temp stack is less than 
        # the curr pick we add it to the temp stack and then continue to go to the next pick
        if not temp_stack or temp_stack[-1] < curr_pick:
            print(f"Temp stack is empty or the top element in the temp stack is lesser than current pick")
            temp_stack.append(curr_pick)
            print(f"After append, temp stack is: {temp_stack}")
            continue
        print(f"Temp stack top value is: {temp_stack[-1]} and curr pick is: {curr_pick}. Going to loop")
        # if temp stack is present the curr pick is smaller then the latest element, we
        # first remove the topmost element in the temp stack and add it to the stack. And 
        # append the curr pick to the temp stack
        while temp_stack and temp_stack[-1] > curr_pick:
            print(f"Remove value from the temp_stack")
            val = temp_stack.pop()
            print("Append it to the stack")
            stack.append(val)
        temp_stack.append(curr_pick)
        print(f"Original stack: {stack}")
        print(f"Temp stack: {temp_stack}")

    return temp_stack
        
        
print(sort_stack(my_stack=stack))