#Traversal
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
    
class doublyLL:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)         # 1. Create a new node
        if self.head is not None:        # 2. If list is not empty
            self.head.prev = new_node    #    - old head's prev points to new node
            new_node.next = self.head    #    - new node's next points to old head
        self.head = new_node             # 3. Update head to new node

    # def insertBegin(self,data):
    #     new_node=Node(data)
    #     new_node.next=self.head
    #     if(self.head):
    #         self.head.prev=new_node
    #     return new_node
    
    def insertAfterNode(self, node, data):
        if node is None:
            print("Error: The given node is None")
        
        new_node = Node(data)
        new_node.prev = node
        new_node.next = node.next

        if new_node.next:
            node.next.prev = new_node #ensures backward link current -> next_node
        
        node.next = new_node
    
    def insertBeforeNode(self, node, data):
        if node is None:
            print("Error: The given node is None")
        
        new_node = Node(data)
        new_node.prev = node.prev
        new_node.next = node

        if new_node.prev:
            node.prev.next = new_node #ensures forward link prev_node -> current (previous node's forward link)
        
        node.prev = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            return new_node
        
        current_node = self.head
        while current_node:
            current_node = current_node.next
        
        current_node.next = new_node
        new_node.prev = current_node
        return self.head
        
    def deleteAtBeginning(self):
        if self.head is None:
            print("Doubly linked list is empty")
            return None
        
        temp = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        del temp

    def deleteAtSpecific(self, pos):
        if self.head is None:
            print("Empty")
            return
        
        current_node = self.head
        index = 0
        while(current_node is not None and index < pos):
            current_node = current_node.next
            index +=1

        if(current_node is None):
            print("Position out of range")
            return
        
        if current_node.prev is not None:
            current_node.prev.next = current_node.next
        if current_node.next is not None:
            current_node.next.prev = current_node.prev

        del current_node

    def deleteAtEnd(self, pos):
        if self.head is None:
            print("Empty")
            return
        
        if self.head.next is None:
            return None
        
        current = self.head
        while(current.next.next):
            current = current.next

        del_node = current.next
        current.next = None
        del del_node
        return self.head

    def printDLL(self):
        current_node=self.head
        while(current_node):
            print(current_node.data, "<->", end=" ")
            current_node=current_node.next
        print("None")

d=doublyLL()
d.insertAtBegin(10)
d.insertAtBegin(20)
d.insertAtBegin(30)
d.insertAtBegin(40)
d.printDLL()
