class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_n  = {}

        counter = 1
        max_num = nums[0]

        for i in range(len(nums)):
            if nums[i] == max_num:
                counter +=1
            elif nums[i] != max_num:
                counter -=1
            if counter == 0:
                max_num = nums[i]
                counter+=1
        return max_num

        # https://leetcode.com/problems/majority-element/