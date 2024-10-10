class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex = rowIndex +1
        dp = [[0] * i for i in range(1,rowIndex+1)]
        

        for r in range(rowIndex):
            dp[r][0] = 1
            dp[r][r] = 1
        
        for r in range(2,rowIndex):
            for c in range(1,len(dp[r])-1):
                dp[r][c] = dp[r-1][c] + dp[r-1][c-1]
        
        return dp[-1]
        