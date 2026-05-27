# A Node only needs to know its data and the next node
class Node:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.next = None  # Points to the next node, None by default

# The LinkedList class manages the nodes
class LinkedList:
    def __init__(self):
        self.head = None  # The head points to the first node, empty by default

    def append(self, data):
        new_node = Node(data)  # Create a new node

        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            return

        current = self.head  # Start at the head
        while current.next:  # Traverse until we find the last node
            current = current.next
        current.next = new_node  # Point the last node to the new node

    def print_list(self):
        current = self.head  # Start at the head
        while current:  # Traverse until we reach None
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Print None at the end to show the list has ended

# Create a linked list and add some nodes
ll = LinkedList()
ll.append("Hello")
ll.append("World")
ll.append("Foo")

ll.print_list()  # Hello -> World -> Foo -> None