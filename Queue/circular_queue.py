class Que:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.rear = self.front = -1

    def enqueue(self, val):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")

        elif(self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = val
        
        else:
            self.rear = (self.rear+ 1) % self.size
            self.queue[self.rear] = val

    def dequeue(self):

        if self.front == -1:
            print("quque is empty")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp

        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1 ) % self.size
            return temp


    
