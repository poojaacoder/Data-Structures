class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 2 dp with O(mn) space and time 
        # dp = [[1] * n ] * m
        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)
        # return dp[-1][-1]

        #  approach 2 , use 1 dp
        # dp = [1] * n
        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[j] += dp[j-1]
        # print(dp)
        # return dp[-1]
        dp = [[0] * n ]*m 

        for i in range(m):
            dp[i][0] = 1

        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

        
        # https://leetcode.com/problems/unique-paths/