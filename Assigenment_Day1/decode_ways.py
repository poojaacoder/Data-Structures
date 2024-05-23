# https://www.youtube.com/watch?v=g1nFbi7bIV0
# https://leetcode.com/problems/decode-ways/description/

def numDecodings(s: str) -> int:
    if s[0] == '0':
        return 0
    dp = [1,1]
    for ind, num in enumerate(s[1:], 2):
        ways = 0
        print(ind, num)
        if num != "0":
            ways += dp[ind-1]
        if 10 <= int(s[ind-2]+num) <= 26:
            print(int(s[ind-2]+num))
            ways+= dp[ind-2]
        dp.append(ways)
    print(dp)
    return dp[-1]


k = "4205"
print(numDecodings(k))


4205
[1, 2, ]
    