class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dp = []
        for n in nums:
            n = abs(n)
            if nums[n-1] < 0:
                dp.append(n)
            nums[n-1] = - nums[n-1]
        return dp

# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/