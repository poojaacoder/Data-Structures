class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        start = 1
        count = 1
        prev = nums[0]
        max_len = 1

        while start < len(nums):
            if nums[start] != prev:
                if nums[start] == prev +1:
                    count +=1
                    prev +=1
                else:
                    prev = nums[start]
                    count =1
                max_len = max(max_len , count)
            start +=1
        return max_len
        
        # https://leetcode.com/problems/longest-consecutive-sequence/