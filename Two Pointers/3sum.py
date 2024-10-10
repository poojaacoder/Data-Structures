class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <3:
            return []

        nums.sort()
        n = len(nums)

        #  for loop for outer 1st ele
        # use binary search for two ele as 2 sum prob
        # duplicate numbers handling
        result = []
        for i in range(0, n-2):
            left = i+1
            right = n-1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                summ = nums[i] + nums[left]+ nums[right]
                if summ == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left +=1
                    right -=1
                elif summ > 0:
                    right -= 1
                elif summ < 0:
                    left +=1
        return result




# https://leetcode.com/problems/3sum/