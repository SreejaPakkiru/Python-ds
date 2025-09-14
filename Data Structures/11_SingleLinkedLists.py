# class Node:
#     data=0
#     next=None

#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class SinglyLL:
#     head=None

#     def insert_at_begin(self,data):
#         new_node=Node(data)

#         if(self.head is None):
#             self.head=new_node
#             return
#         new_node.next=self.head
#         self.head=new_node
    
        
# sl=SinglyLL()
# sl.insert_at_begin(10)
# print(sl.head.data)
# sl.insert_at_begin(20)
# sl.insert_at_begin(30)
# print(sl.head.data)
# print(sl.head.next.data)

#Creating a Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insertAtSpecific(self,data,index):
        if (index == 0):
            self.insertAtBegin(data)
        
        position=0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position+1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    def insertAtEnd (self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while(current_node.next): #or while current_node.next is not None
            current_node = current_node.next
        current_node.next = new_node #attcaching new node to end
    
    def deleteAtBegin(self):
        if(self.head is None):
            return# print("No nodes to remove")
        
        self.head = self.head.next

    def deleteAtEnd(self):
        if(self.head == None):
            return
        
        current_node = self.head
        while(current_node.next != None or current_node.next.next != None):
            current_node = current_node.next #traverse nodes

        current_node.next = None

    def deleteAtSpecific(self, data, index):
        if (self.head==None):
            return
        current_node = self.head
        position=0
        if index == 0:
            self.deleteAtBegin()
        else:
            while(current_node != None or position < index-1):
                position +=1
                current_node.next

            if current_node is None or current_node.next is None:
                print("Index not present")
            else:
                current_node.next = current_node.next.next

    def UpdateLL(self, val, index):
        current_node = self.head
        position = 0
        if position==index:
            current_node.data = val
        else:
            while( current_node != None and position !=None):
                position = position+1
                current_node = current_node.next
            if current_node != None:
                current_node.data = val
            else:
                print(" Index not found")

    def sizeLL(self):
        size=0
        current_node = self.head
        while(current_node == None):
            size+=1
            current_node=current_node.next
        return size

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")
                
l=LinkedList()
# add first few nodes
l.insertAtBegin("C")      # C
l.insertAtBegin("B")      # B → C
l.insertAtBegin("A")
l.insertAtSpecific("D",1)
# l.insertAtSpecific(10,0)
# l.insertAtSpecific(20,1)
# l.insertAtSpecific(30,2)
# l.insertAtSpecific(40,3)
l.printLL()# A → D → B → C → None
l.insertAtEnd("D")
l.printLL()
l.deleteAtBegin()
l.printLL()
l.UpdateLL("F",0)
l.printLL()
print(l.sizeLL())