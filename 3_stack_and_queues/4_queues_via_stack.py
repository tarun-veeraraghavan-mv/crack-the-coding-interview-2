"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""

class QueueViaStack():
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, val: int):
        self.stack_in.append(val)

    def pop(self):
        if not self.stack_in:
            return None

        # reverse the order
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        # pop the item
        return self.stack_out.pop()
    
my_queue_via_stack = QueueViaStack()

my_queue_via_stack.push(val=2)
my_queue_via_stack.push(val=3)
my_queue_via_stack.push(val=4)

print(my_queue_via_stack.stack_in)
print(my_queue_via_stack.stack_out)

my_queue_via_stack.pop()

print(my_queue_via_stack.stack_in)
print(my_queue_via_stack.stack_out)

my_queue_via_stack.push(val=5)

print(my_queue_via_stack.stack_in)
print(my_queue_via_stack.stack_out)

my_queue_via_stack.pop()

print(my_queue_via_stack.stack_in)
print(my_queue_via_stack.stack_out)