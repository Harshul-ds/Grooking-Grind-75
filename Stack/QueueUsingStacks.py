class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()

class MyQueue:
    def __init__(self):
        self.enqueueStack = []  # Stack to push elements into
        self.dequeueStack = []  # Stack to pop elements from

    def push(self, x):
        self.enqueueStack.append(x)  # Push element onto enqueue stack

    def pop(self):
        if not self.dequeueStack:  # If dequeue stack is empty
            # Transfer elements from enqueue stack to dequeue stack
            while self.enqueueStack:
                self.dequeueStack.append(self.enqueueStack.pop())
        return self.dequeueStack.pop()  # Pop element from dequeue stack

    def peek(self):
        if not self.dequeueStack:  # If dequeue stack is empty
            # Transfer elements from enqueue stack to dequeue stack
            while self.enqueueStack:
                self.dequeueStack.append(self.enqueueStack.pop())
        return self.dequeueStack[-1]  # Return the top element of dequeue stack without popping it

    def empty(self):
        return not self.enqueueStack and not self.dequeueStack  # Queue is empty if both stacks are empty

