import heapq
from collections import List
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        projects = [(capital[i], profits[i]) for i in range(len(capital))]

        projects.sort()
        print(projects)
        max_heap = []

        n = len(projects)
        j = 0
        for _ in range(k):
            while j < n and projects[j][0] <= w:
                heapq.heappush(max_heap, -projects[j][1])
                j+=1
            
            if not max_heap:
                break
            
            w -=heapq.heappop(max_heap)
        return w
        

        # https://leetcode.com/problems/ipo/?envType=problem-list-v2&envId=heap-priority-queue