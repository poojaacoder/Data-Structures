class MinStack:

    def __init__(self):
        self.stack = []
        self.min_s =[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_s or val <= self.min_s[-1]:
            self.min_s.append(val)


        

    def pop(self) -> None:
        if self.stack.pop() == self.min_s[-1]:
            self.min_s.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_s[-1]
        

# https://leetcode.com/problems/min-stack/submissions/1261361508/
# Your min_s object will be instantiated and called as such:
# obj = min_s()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()