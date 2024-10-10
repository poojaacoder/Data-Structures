class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #  its between 1 to n 
        #  sum of numbers from 1 to n 
        #  1. can be done using two for loops , but that would be O(n2)
        #  2.  can be done using two pointer , with linear complexity , slow and fast ptr
        #  3. best way is to xor, same bit will be noticed and diff will be ignored
        #  first go through list value then the n 
        # res = 0
        # for n in nums:
        #     res ^= n
        # for i in range(1,len(nums)):
        #     res ^= i
        # return res

        # 4. mark the number's index number as -1 

        i = 0
        while True:
            i = abs(nums[i])
            if nums[i] < 0:
                return i
            nums[i] = -1 * nums[i]

            #  O(n), (1)
            
        # https://leetcode.com/problems/find-the-duplicate-number/