import collections
import heapq
import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        output = 0
        h = []
        count = collections.Counter(tasks)
        for t, freq in count.items():
            heapq.heappush(h, (-freq, t))
        
        while h:
            i = 0
            temp = []
            while i <= n:
                output +=1
                if h :
                    num, t = heapq.heappop(h)
                    num +=1 
                    if num <0 : temp.append((num, t))
                
                if not h and not temp:
                    break
                i+=1
            for num, t in temp:
                heapq.heappush(h, (num, t))
        return output
        
# https://leetcode.com/problems/task-scheduler/?envType=problem-list-v2&envId=heap-priority-queue