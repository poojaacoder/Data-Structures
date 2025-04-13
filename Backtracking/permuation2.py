class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def cal(path, dp):
            if len(path) == len(nums):
                ans.add(tuple(path[:]))
                return 
            for i in range(len(nums)):
                if dp[i] == 1:
                    continue
                dp[i] = 1
                cal(path+[nums[i]],dp )
                dp[i] = 0      
        dp = [0] * len(nums)
        ans = set()
        cal([], dp)
        return list(a for a in ans)
        

        # https://leetcode.com/problems/permutations-ii/?envType=problem-list-v2&envId=backtracking