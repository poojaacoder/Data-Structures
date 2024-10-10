class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        #  create dp 
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols  for _ in range(rows)]

        dp[0][0] = grid[0][0]
        # 1, update first row 
        for c in range(1,cols):
            dp[0][c] = dp[0][c-1] + grid[0][c]

        # update first col
        for r in range(1, rows):
            dp[r][0] = dp[r-1][0] + grid[r][0]

        #  calculate distance by adding i-1, j and j-1, i
        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
        
        return dp[rows-1][cols-1]



        