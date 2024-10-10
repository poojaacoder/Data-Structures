class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = 0
        while i < len(nums):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
            i+=1
        return k



        
# https://leetcode.com/problems/remove-element/