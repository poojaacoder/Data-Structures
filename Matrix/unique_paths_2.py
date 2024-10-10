class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # return 0 if 00 and rows cols has 1 , that shpows there is obstacle in start and end 
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        # create dp with 1 as input 
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0] * cols for _ in range(rows)]

        dp[0][0] = 1

        # update first col
        for r in range(1, rows):
            if obstacleGrid[r][0] == 0:
                dp[r][0] = dp[r-1][0]
            else:
                dp[r][0] = 0


        # update first row
        for c in range(1, cols):
            if obstacleGrid[0][c] == 0:
                dp[0][c] = dp[0][c-1]
            else:
                dp[0][c] = 0

        print(dp)
        # count the paths  i-1 , j + i., j-1 + to come to any point
        for r in range(1,rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
                else:
                    dp[r][c] = 0

        # get the last dp[rows][cols] as output
    
        print(dp)
        return dp[rows-1][cols-1]
    

    # https://leetcode.com/problems/unique-paths-ii/