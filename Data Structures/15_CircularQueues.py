class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1

    def is_Empty(self):
        return self.front ==-1
    
    def is_Full(self):
        return (self.rear + 1) % self.max_size == self.front
    
    def enqueue(self, data):
        if self.is_Full():
            print("Queue is full")
            return
        
        if self.is_Empty():
            self.front = 0
        
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = data
        print(f"{data} inserted")

    def dequeue(self):
        if self.is_Empty():
            print("Queue is empty")
            return
        
        removed = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        
        else:
            self.front = (self.front + 1) % self.max_size

        print(f"{removed} removed")
        return removed
    
    def dispaly(self):
        if self.is_Empty():
            print("Queue is Empty")
            return
        
        i = self.front
        while(True):
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i+1) % self.max_size
        print()

c = CircularQueue(3)
c.enqueue(1)
c.enqueue(2)
c.dequeue()
c.dispaly()
