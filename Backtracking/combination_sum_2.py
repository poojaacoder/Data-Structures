class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        def cal(ind, arr, t):
            if t == 0:
                ans.append(arr[:])
                return 
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > t:
                    break
                cal(i+1, arr+ [candidates[i]], t- candidates[i])
        
        candidates.sort()
        cal(0, [], target)
        return ans
        
        # https://leetcode.com/problems/combination-sum-ii/?envType=problem-list-v2&envId=backtracking