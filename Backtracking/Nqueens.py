class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        neg_dig = set()
        pos_dig  = set()


        board = [['.'] * n for i in range(n)]
        ans = []

        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                ans.append(copy)
                return
            
            for c in range(n):

                if c in col or (r+c) in pos_dig or (r-c) in neg_dig:
                    continue
                col.add(c)
                neg_dig.add(r-c)
                pos_dig.add(r+c)

                board[r][c] = 'Q'
                backtrack(r+1)


                col.remove(c)
                neg_dig.remove(r-c)
                pos_dig.remove(r+c)
                board[r][c] = '.'
    
        backtrack(0)
        return ans
    

    # https://leetcode.com/problems/n-queens/?envType=problem-list-v2&envId=backtracking