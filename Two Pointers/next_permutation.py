from itertools import permutations 
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #  find the first ele from right ie not in decreasing order ie i 
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i-=1
        
        # if found, find smallest from right ie greate that previous result,
        #  otherwise just reverse
        if i >=0:
            j = len(nums)-1
            while nums[j] <= nums[i]:
                j -=1
            nums[i], nums[j] = nums[j], nums[i]
            # and swap it with previous
        # reverse the number for i + 1 to the end
        nums[i+1:] = reversed(nums[i+1:])

        # 


        
# https://leetcode.com/problems/next-permutation/