from collections import deque
import heapq
class Solution:
    def maxSlidingWindow(self, nums, k):
        def getmax(q):
            heapq._heapify_max(q)
            return q[0]

        q = deque()
        max_window_val = []
        for i in range(len(nums)):
            q.append(nums[i])
            if len(q) > k:
                q.popleft()
                max_window_val.append(getmax(list(q)))
        return max_window_val


        

# https://leetcode.com/problems/sliding-window-maximum/?envType=problem-list-v2&envId=heap-priority-queue