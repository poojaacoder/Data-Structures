class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = set()
        def cal(ind, arr):

            if ind == len(nums):
                ans.add(tuple(arr[:]))
                return

            cal(ind+1, arr+[nums[ind]])
            cal(ind+1, arr)

        # def cal(ind, arr):
        #     ans.append(arr[:])
        #     for i in range(ind, len(nums)):
        #         if i > ind and nums[i] == nums[i-1]:
        #             continue
        #         cal(i+1, arr + [nums[i]])

        nums.sort()
        cal(0, [])
        return [list(a) for a in ans]
    
    # https://leetcode.com/problems/subsets-ii/?envType=problem-list-v2&envId=backtracking