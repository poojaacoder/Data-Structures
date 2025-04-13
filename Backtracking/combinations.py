class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def combine(ind, path):
            if len(path) == k:
                res.append(path[:])
                return 
            for num in range(ind, n+1):
                path.append(num)
                combine(num+1, path)
                path.pop()

        res = []
        path = []
        combine(1, path)
        return res
    
    # https://leetcode.com/problems/combinations/?envType=problem-list-v2&envId=backtracking