class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0
        dp [1] = 1
        if n <= 3:
            return n
        for i in range(2, n+1):
            j = 1
            while(j*j) <= i:
                dp[i] = min(dp[i], 1+ dp[i- (j*j)])
                j +=1
        return dp[n]



        # https://leetcode.com/problems/perfect-squares/