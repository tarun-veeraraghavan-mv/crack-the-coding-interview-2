"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStack s that mimics this. SetOfStack s should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStack s .push() and SetOfStack s .pop() should behave identically to a single stack
(that is, pop( ) should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt( in t index ) which performsa pop operation on a specific sub-stack.
"""

class StackOfPlates():
    def __init__(self, threshold: int):
        self.threshold = threshold
        self.stack_of_plates = [[]]
        self.current_stack_index = 0

    def push(self, val: int):
        curr_stack = self.stack_of_plates[self.current_stack_index]
        curr_stack.append(val)
        # logic when the threshold is less than 10
        if len(curr_stack) == self.threshold:
            # get the current stack at the index
            self.stack_of_plates.append([])
            self.current_stack_index += 1
            
    def pop(self):
        curr_stack = self.stack_of_plates[self.current_stack_index]

        val = curr_stack.pop()

        # if not the first stack
        if len(curr_stack) == 0 and self.current_stack_index > 0:
            self.current_stack_index -= 1
            self.stack_of_plates.pop()


        if self.current_stack_index == 0 and len(curr_stack) == 0:
            self.current_stack_index = 0
            self.stack_of_plates = [[]]

        return val
        
