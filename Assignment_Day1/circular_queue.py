class MyCircularQueue:

    def __init__(self, k: int):
        self.queue= [None] * k
        self.size = k
        self.front = self.rear = -1
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif(self.front == -1):
            self.front = self.rear = 0
            self.queue[self.rear] = value
            return True
        else:
            self.rear = (self.rear +1) % self.size
            self.queue[self.rear] = value
            return True

        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.front == self.rear :
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return True
        else:
            temp = self.queue[self.front]
            self.front = (self.front+1) % self.size
            return True
        

    def Front(self) -> int:
        if self.isFull():
            return -1
        else:
            return self.queue[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        return self.front == -1 
        

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size ==  self.front
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()