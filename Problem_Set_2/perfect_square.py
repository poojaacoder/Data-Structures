def numSquares(n: int) -> int:
    if n <= 3:
        return n
    res = n
    for x in range(1, n + 1):
        print("print x :", x)
        temp = x * x
        if temp > n:
            break
        else:
            res = min(res, 1 + numSquares(n-temp))
            print(res,  numSquares(n-temp))
    
    return res

#  O(n2)
# n = 5
# print(numSquares(n))


def numSquares_dp(n):
    dp = [n] * (n + 1)  
    dp[0] = 0  
    dp[1] = 1  # 1^2
    print(dp)
    for i in range(2, n + 1):
      j = 1
      while j * j <= i:
        print(dp[i], dp[i - j * j] + 1, i, j)
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        
        j += 1
        print(dp)

    return dp[n]


n = 5
print(numSquares_dp(n))

        # time complexity : O(log n)
        # space complexity : O(n log n)