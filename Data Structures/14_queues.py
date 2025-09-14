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
q1= Queue(maxsize = 3)
print(q.qsize()) 
q1.put('a')
q1.put('b')
q1.put('c')
print(q1.full()) 
print(q1.get())
print(q1.get())
print(q1.get())
print(q1.empty())
q1.put(1)
print(q1.empty()) 
print(q1.full())

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

class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to the queue")

    # Dequeue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue.pop(0)

    # Peek / Front
    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[0]

    # Check if empty
    def is_empty(self):
        return len(self.queue) == 0

    # Size
    def size(self):
        return len(self.queue)

    # Display
    def display(self):
        print("Queue:", self.queue)


# ---------------------------
# Usage
q2 = Queue()
q2.enqueue('A')
q2.enqueue('B')
q2.enqueue('C')
q2.display()

print("Dequeued:", q2.dequeue())
q2.display()

print("Front element:", q2.front())
print("Size:", q2.size())
