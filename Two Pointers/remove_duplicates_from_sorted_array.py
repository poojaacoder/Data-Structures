class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums :
            return 0
        if len(nums) == 1:
            return 1
    
        k = 0
        nums[k] = nums[0]
        k +=1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]                                                                                                                                        
                k += 1
        return k
        
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/