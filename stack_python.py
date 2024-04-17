from queue import Queue

class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, value):
        # Add the new element to the empty queue
        if self.queue1.empty():
            self.queue1.put(value)
            while not self.queue2.empty():
                self.queue1.put(self.queue2.get())
        else:
            self.queue2.put(value)
            while not self.queue1.empty():
                self.queue2.put(self.queue1.get())

    def pop(self):
        # Pop from the non-empty queue
        if not self.queue1.empty():
            return self.queue1.get()
        elif not self.queue2.empty():
            return self.queue2.get()
        else:
            return None

    def top(self):
        if not self.queue1.empty():
            return self.queue1.queue[0]
        elif not self.queue2.empty():
            return self.queue2.queue[0]
        else:
            return None

    def is_empty(self):
        return self.queue1.empty() and self.queue2.empty()

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top of the stack:", stack.top())  # Output: 3

print("Pop from stack:", stack.pop())    # Output: 3
print("Pop from stack:", stack.pop())    # Output: 2
print("Pop from stack:", stack.pop())    # Output: 1

print("Is stack empty?", stack.is_empty())  # Output: True
