class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def map_linked_list(head, mapping_function):
    if head is None:
        return None

    new_head = Node(mapping_function(head.data))
    current = new_head
    head = head.next

    while head:
        current.next = Node(mapping_function(head.data))
        current = current.next
        head = head.next

    return new_head

original_list = Node(1, Node(2, Node(3)))

def mapping_function(x):
    return x * 2

mapped_list = map_linked_list(original_list, mapping_function)

current = mapped_list
while current:
    print(current.data, end=" -> ")
    current = current.next


