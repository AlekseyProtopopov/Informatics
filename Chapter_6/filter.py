class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def filter_linked_list(head, predicate_function):
    if head is None:
        return None

    new_head = None
    new_current = None
    
    current = head
    while current:
        if predicate_function(current.data):
            new_node = Node(current.data)
            if new_head is None:
                new_head = new_node
                new_current = new_node
            else:
                new_current.next = new_node
                new_current = new_node
        current = current.next
    
    return new_head

original_list = Node(1, Node(2, Node(3)))

def predicate_function(x):
    return x >= 2

filtered_list = filter_linked_list(original_list, predicate_function)

current = filtered_list
while current:
    print(current.data, end=" -> ")
    current = current.next
# Ожидаемый вывод: 2 -> 3 -> 

