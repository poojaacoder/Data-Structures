class RollingAVg:
    
    def __init__(self, k):
        self.k = k
        self.queue = deque()
        self.sum = 0


        def getAvg(self, latency):
            self.queue.append(latency)
            self.sum += latency
            if len(self.queue) > k :
                rm = self.queue.popleft()
                self.sum -= rm
            
            return sum // len(self.queue)
            
            
            
            
            

            
        