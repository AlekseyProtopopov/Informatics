class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

def count(head, value):
    count = 0
    current = head
    while current:
        if current.data == value:
            count += 1
        current = current.next
    return count

list1 = Node(1, Node(2, Node(3)))
result_length = length(list1)
print(result_length)  

result_count = count(list1, 1)
print(result_count)  

list2 = Node(1, Node(1, Node(1, Node(2, Node(2, Node(2, Node(2, Node(3, Node(3)))))))))
result_count_2 = count(list2, 2)
print(result_count_2)  

