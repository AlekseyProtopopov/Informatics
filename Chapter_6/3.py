class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node  
            return
        last_node = self.head
        while last_node.next:  
            last_node = last_node.next
        last_node.next = new_node  

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  
        self.head = new_node 

    def delete(self, data):
        if self.is_empty():
            return
        
        if self.head.data == data: 
            self.head = self.head.next 
            return

        current_node = self.head
        while current_node.next:  
            if current_node.next.data == data:  
                current_node.next = current_node.next.next  
                return
            current_node = current_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

my_linked_list = LinkedList()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.prepend(0)

my_linked_list.display()

my_linked_list.delete(2)

my_linked_list.display()
