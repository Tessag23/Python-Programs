class Node:
    def __init__(p, data):
        p.item = data
        p.next = None
        p.prev = None
# Class for doubly Linked List
class doublyLinkedList:
    def __init__(p):
        p.head = None
    # Insert element at the end
    def InsertToEnd(p, data):
        # Check if the list is empty
        if p.head is None:
            new_node = Node(data)
            p.head = new_node
            return
        n = p.head
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    # Traversing and Displaying each element of the list
    def Display(p):
        if p.head is None:
            print("The list is empty")
            return
        else:
            print('elements are ',end='')
            n = p.head
            while n is not None:
                print( n.item,end=' ')
                n = n.next
# Create a new Doubly Linked List
NewDoublyLinkedList = doublyLinkedList()
# Insert the element at the end
NewDoublyLinkedList.InsertToEnd(20)
NewDoublyLinkedList.InsertToEnd(30)
NewDoublyLinkedList.InsertToEnd(40)
NewDoublyLinkedList.InsertToEnd(50)
NewDoublyLinkedList.InsertToEnd(60)
# Display Data
NewDoublyLinkedList.Display()