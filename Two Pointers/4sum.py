import collections
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        resultSet = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):           
                tempset = set()
                for k in range(j+1, len(nums)):
                    summ = nums[i] + nums[j] + nums[k]
                    fourth = target - summ
                    if fourth in tempset:
                        res = [nums[i], nums[j], nums[k], fourth]
                        res.sort()
                        print(res)
                        resultSet.add(tuple(res))
                    tempset.add(nums[k])
        return [list(item) for item in resultSet]


# https://leetcode.com/problems/4sum/