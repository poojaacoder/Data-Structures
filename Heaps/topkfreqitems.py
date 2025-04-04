import collections
import heapq
class Solution:
    def topKFrequent(self, nums, k: int):
        freq = collections.defaultdict(int)
        output = []

        for n in nums:
            freq[n] +=1
        
        min_heap = []
        for num, freq in freq.items():
            heapq.heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        for freq, num in min_heap:
            output.append(num)
        return output
    
# https://leetcode.com/problems/top-k-frequent-elements/submissions/1570393409/?envType=problem-list-v2&envId=heap-priority-queue