"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum eiement? Push, pop and min should ail operate in 0(1 ) time.
"""

class MyStack():
    def __init__(self):
        self.stack = []
        # stack to keep track of the minimum values being pushed.. the min value will be at the top of the stack
        self.min_stack = []

    def push(self, val: int):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if self.min_stack[-1] == val:
            self.min_stack.pop()

    def min(self):
        return self.min_stack[-1]
    