# Implementation using list
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print(queue)
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue)

# Implementation using Collections.Deque
from collections import deque
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
print(q.popleft())
print(q)

# Implementation using queue.Queue
from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize()) 
q.put('a')
q.put('b')
q.put('c')
print(q.full()) 
print(q.get())
print(q.get())
print(q.get())
print(q.empty())
q.put(1)
print(q.empty()) 
print(q.full())

#Queue implementation using Classes
# class Queue:
#     def __init__(self):
#         self.items = []

#     # Enqueue: Add element at the end
#     def enqueue(self, item):
#         self.items.append(item)

#     # Dequeue: Remove element from the front
#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         return "Queue is empty"

#     # Peek: Show front element
#     def peek(self):
#         if not self.is_empty():
#             return self.items[0]
#         return "Queue is empty"

#     # Check if empty
#     def is_empty(self):
#         return len(self.items) == 0

#     # Display queue
#     def display(self):
#         print("Queue:", self.items)


# # Example usage
# q = Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.display()          # Queue: [10, 20, 30]

# print(q.dequeue())   # 10
# q.display()          # Queue: [20, 30]

# print("Front element:", q.peek())  # 20
