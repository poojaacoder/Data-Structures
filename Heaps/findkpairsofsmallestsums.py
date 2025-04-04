import List
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        min_heap = []
        output = []

        for i in range(min(k, len(nums1))):
            summ = nums1[i] + nums2[0]
            heapq.heappush(min_heap, (summ, i, 0))

        while min_heap and len(output) < k:
            _, i, j = heapq.heappop(min_heap)
            output.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                cur_sum = nums1[i] + nums2[j+1]
                heapq.heappush(min_heap, (cur_sum, i, j+1))

        return output

# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/?envType=problem-list-v2&envId=heap-priority-queue
