class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        def cal(ind, arr, t):
            # exit condition
            if ind == len(candidates):
                if t == 0:
                    ans.append(arr[:])
                return

            # pick number
            if candidates[ind] <= t:
                cal(ind, arr+[candidates[ind]], t - candidates[ind])

            # dont pick number
            cal(ind+1, arr, t)

        cal(0,[], target)
        return ans
        
        # https://leetcode.com/problems/combination-sum/?envType=problem-list-v2&envId=backtracking