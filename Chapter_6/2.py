class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item, priority=5):
        self.items.append((item, priority))
        self.sort_queue()  

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")  
        return self.items.pop(0) 

    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue") 
        return self.items[0]

    def size(self):
        return len(self.items)

    def sort_queue(self):
        self.items.sort(key=lambda x: x[1])  

my_queue = Queue()

my_queue.enqueue(1, priority=2)
my_queue.enqueue(2, priority=5)
my_queue.enqueue(3, priority=0)

print("Queue:", my_queue.items)

dequeued_item = my_queue.dequeue()
print("Dequeued item:", dequeued_item)

front_item = my_queue.front()
print("Front item:", front_item)

my_queue.enqueue(4, priority=3)
print("Queue after enqueue:", my_queue.items)

print("Is queue empty?", my_queue.is_empty())

print("Queue size:", my_queue.size())
