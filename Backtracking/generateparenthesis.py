class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        def cal(open_count, close_count, strs):
            if len(strs) == 2*n:
                ans.append(strs)
                return
            if open_count < n:
                cal(open_count+1, close_count, strs+'(')
            if close_count < open_count:
                cal(open_count, close_count+1, strs+')')   
        cal(0,0, '')
        return ans