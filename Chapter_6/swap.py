
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def linked_list(*values):
    linked_list = LinkedList()
    for value in values:
        new_node = Node(value)
        if not linked_list.head:
            linked_list.head = new_node
        else:
            current = linked_list.head
            while current.next:
                current = current.next
            current.next = new_node
    return linked_list

def print_linked_list(linked_list):
    current = linked_list.head
    output = []
    while current:
        output.append(str(current.value))
        current = current.next
    print(" -> ".join(output) + " -> None")

def get_node_and_prev(linked_list, index):
    current = linked_list.head
    prev = None
    count = 0
    while current:
        if count == index:
            return current, prev
        prev = current
        current = current.next
        count += 1
    return None, None

def swap_nodes(list_pointer1, index1, list_pointer2, index2):
    list1 = list_pointer1[0]
    list2 = list_pointer2[0]
    
    node1, prev1 = get_node_and_prev(list1, index1)
    node2, prev2 = get_node_and_prev(list2, index2)

    if not node1 or not node2:
        return False

    if prev1:
        prev1.next = node2
    else:
        list1.head = node2

    if prev2:
        prev2.next = node1
    else:
        list2.head = node1

    node1.next, node2.next = node2.next, node1.next
    
    return True


list1 = linked_list(1, 2, 3, 4)
list2 = linked_list(5, 6, 7, 8)

result = swap_nodes([list1], 2, [list2], 0)
print(result)  

print_linked_list(list1)


print_linked_list(list2)


list1 = linked_list(1, 2, 3)
list2 = linked_list(4, 5, 6)

result = swap_nodes([list1], 1, [list2], 3)
print(result)  

print_linked_list(list1)


print_linked_list(list2)



