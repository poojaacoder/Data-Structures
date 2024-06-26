# https://www.youtube.com/watch?v=g1nFbi7bIV0
# https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n + [1]
        def isValid(a, b=None):
            if b:
                return ( a == '1') or (a =='2') and  (b < '7')
            return a != '0'
        
        if isValid(s[-1]):
            dp[n-1] = 1
        print(dp)
        for i in reversed(range(n-1)):
            if isValid(s[i]):
                dp[i] += dp[i+1]
            if isValid(s[i], s[i+1]):
                dp[i] += dp[i+2]
            print(dp)
        return dp[0]
