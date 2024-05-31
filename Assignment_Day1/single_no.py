class Solution:
    def singleNumber(self, nums) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

        
