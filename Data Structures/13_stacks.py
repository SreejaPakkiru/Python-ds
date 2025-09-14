# #Implementation using list
# stack = []
# stack.append('a')
# stack.append('b')
# stack.append('c')
# print(stack)
# stack.pop()
# print(stack) #['a', 'b']

# #Implementation using Deque
# from collections import deque
# stackq = deque()
# stackq.append(1)
# stackq.append(2)
# stackq.append(3)
# print(stackq) 
# stackq.pop()
# print(stackq) #deque([1, 2])

# #Implementation using Queue module
# from queue import LifoQueue
# stack1 = LifoQueue(maxsize=4)
# print(stack1.qsize())
# stack1.put(1)
# stack1.put(2)
# stack1.put(3)
# stack1.put(4)
# print(stack1.full())
# print(stack1.qsize())
# print(stack1.get())
# print(stack1.full())
# print(stack1)  #<queue.LifoQueue object at 0x00000130FB7E5010>

class Stack:
    def __init__(self, size):
        self.size = size
        self.stackArray = []
        self.top = -1
    
    def push(self, data):
        if(self.isFull()):
            print("stack is full")
            return
        
        self.stackArray.append(data)
    
    def isFull(self):
        return self.size == self.top
    
# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]

#     def is_empty(self):
#         return len(self.items) == 0

#     def size(self):
#         return len(self.items)

# # Example
# s = Stack()
# s.push(5)
# s.push(10)
# print("Top element:", s.peek())
# print("Popped:", s.pop())
# print("Size:", s.size())

    
stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)