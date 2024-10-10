class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum == target:
                return [l+1, r+1]
            elif cur_sum < target:
                l +=1
            else:
                r -=1
        return []


        # https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/