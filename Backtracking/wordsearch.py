class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])


        def dfs(r, c, board, ind):
            if ind == len(word):
                return True
            if r >= len(board) or r <0 or c >= len(board[0]) or c <0 or board[r][c] != word[ind]:
                return False
            temp = board[r][c]
            board[r][c] = '.'
            found = dfs(r-1, c, board, ind+1) or dfs(r, c-1, board, ind+1) or dfs(r+1, c, board, ind+1) or dfs(r, c+1, board, ind+1)
            board[r][c] = temp
            return found

        

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, board, 0):
                        return True
        return False
        

        # https://leetcode.com/problems/word-search/?envType=problem-list-v2&envId=backtracking