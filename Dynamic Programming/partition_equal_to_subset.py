class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        result = set()
        result.add(0)
        for n in nums:
            temp = set()
            for val in result:
                s  = n + val
                if s == target:
                    return True
                if s not in temp:
                    temp.add(s)
            result.update(temp)
        return False
    
    # https://leetcode.com/problems/partition-equal-subset-sum/description/