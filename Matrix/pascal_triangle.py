class Solution:
    def generate(self, numRows: int) -> List[List[int]]: 

        dp = [[0] * i for i in range(1,numRows+1)]
        

        for r in range(numRows):
            dp[r][0] = 1
            dp[r][r] = 1
        
        for r in range(2,numRows):
            for c in range(1,len(dp[r])-1):
                dp[r][c] = dp[r-1][c] + dp[r-1][c-1]
        
        return dp

            

        