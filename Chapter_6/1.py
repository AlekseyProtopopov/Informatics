class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")  
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack.items)

popped_item = my_stack.pop()
print(popped_item)

top_item = my_stack.peek()
print(top_item)

print(my_stack.is_empty())

print(my_stack.size())
