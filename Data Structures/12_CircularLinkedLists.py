class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLL:
    def __init__(self):
        self.head = None
    
    def insertatBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        last_node = self.head
        while(last_node.next != self.head):
            last_node = last_node.next

        new_node.next = self.head
        last_node.next = new_node
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next

        last_node.next = new_node
        new_node.next = self.head

    def insertAfter(self, key, data):
        if self.head is None:
            return
        
        current_node = self.head
        while True:
            if current_node.data == key:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
            if current_node == self.head:
                break

        print("Node not present")

    def printCLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end="->")
            current_node = current_node.next
            if current_node == self.head:
                break

        print("None")

    # DELETE AT BEGINNING
    def deleteAtBegin(self):
        if self.head is None:
            print("List is empty")
            return
        
        # If only one node
        if self.head.next == self.head:
            self.head = None
            return
        
        # Find last node
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        
        # Point last node to 2nd node
        last_node.next = self.head.next
        self.head = self.head.next

    #DELETE AT END 
    def deleteAtEnd(self):
        if self.head is None:
            print("List is empty")
            return
        
        # If only one node
        if self.head.next == self.head:
            self.head = None
            return
        
        prev = None
        current = self.head
        while current.next != self.head:
            prev = current
            current = current.next
        
        # current is last node, prev is second last
        prev.next = self.head

    # DELETE SPECIFIC NODE 
    def deleteNode(self, key):
        if self.head is None:
            print("List is empty")
            return

        # If head is to be deleted
        if self.head.data == key:
            if self.head.next == self.head:  # only one node
                self.head = None
                return
            
            # find last node to fix its next
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            last_node.next = self.head.next
            self.head = self.head.next
            return

        # Delete a non-head node
        prev = self.head
        current = self.head.next
        while current != self.head:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print("Node not found")

    
c=CircularLL()
c.insertatBegin('A')
c.printCLL()
c.insertatBegin('B')
c.printCLL()
c.insertAtEnd('C')
c.printCLL()
c.deleteAtBegin()
c.printCLL()
c.insertAfter('B','D')
c.printCLL()
