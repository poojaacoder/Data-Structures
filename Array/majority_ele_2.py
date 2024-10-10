class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # input nums  => array, can conatain negative numbers 
        #  output => array , number who appread more than once
        #  solve with linear time and constant space 
        #  approach one use extra space ie n and calculate indexes => O(n) time and O(n) space
        #  approach two , sort the numbers  and traverse the list counting the consequestive same numners
        #  time -> O(log n ) + O(n), space , just constant

        # calcualte freq 
        freq = len(nums) // 3
        count = 0
        result = []

        # declare last 
        last = float('-inf')

        # sort the array 
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == last: # check if the last one is same
                count +=1
            else:
                count = 0
                last = nums[i]
            if count == freq:   # check the cur number appear same as desried freq
                result.append(nums[i])
            print(count, last, result)
        return result




        # https://leetcode.com/problems/majority-element-ii/