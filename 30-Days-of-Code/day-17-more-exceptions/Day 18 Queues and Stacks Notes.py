# __STACKS__
# Data Structure that uses LIFO (Last-In-First-Out): last object added to stack must
# be first object removed 
# 3 Operations:
#     1. Peek: return object at top of stack w/o removing it.
#     2. Push: add object passed as argument to top of stack
#     3. Pop: remove object at top of stack and return it.

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

s = Stack()
s.push("A") #A at bottom of stack
s.push("B") #B at top of stack
print(s.peek())

# __Queues__
# Queue: Data Structure uses FIFO (First-In-First-Out): first object added to queue, must be first
# object removed
# Container of Data items/commands that are waiting to be retreived
# What save data if it's not modified
# 2 Operations:
#      1. Enqueue: add object to back of line.
#      2. Dequeue: remove object at head of line and return it.
#      Time complexity: O(1)
# ex. used for printer
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self, item):
        self.items.pop(0)
    
    def front(self):
        if not self.isempty():
            return self.items[0]

    def is_empty(self):
        return self.items == []

# class variable: variable class has by default; always true for class
# instance variable: unique to each object; under the __init__ method
