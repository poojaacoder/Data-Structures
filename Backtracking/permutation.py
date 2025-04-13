class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def cal(path, dp):
            if len(path) == len(nums):
                ans.append(path[:])
                return 
            for i in range(len(nums)):
                if dp[i] == 1:
                    continue
                dp[i] = 1
                cal(path+[nums[i]],dp )
                dp[i] = 0      
        dp = [0] * len(nums)
        ans = []
        cal([], dp)
        return ans  
    
    # https://leetcode.com/problems/permutations/?envType=problem-list-v2&envId=backtracking