class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reduce(head, func, initial_value):
    current = head
    acc = initial_value
    while current:
        acc = func(acc, current.data)
        current = current.next
    return acc

def add(acc, curr):
    return acc + curr

list1 = Node(1, Node(2, Node(3)))
result1 = reduce(list1, add, 0)
print(result1)  # Вывод: 6

def multiply(acc, curr):
    return acc * curr

list2 = Node(1, Node(2, Node(3, Node(4))))
result2 = reduce(list2, multiply, 1)
print(result2)  

