def change(amount: int, coins) -> int:
    dp = [0] * (amount +1)
    dp[0] = 1
    print(dp)
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
            print(dp, i)

    print(dp)
    return dp[amount]



#  time complexity : O(n*m) = n is coins , m i amount
#  space complexity O(n) = dp size
amount = 5
coins =[1,2,5]
print(change(amount, coins))


"""

[1,2 ,5 ]
coin   i       i      1 0 0 0 0 0
1     1,5      1        0 0 0 0 0
                2

 2     2, 5           1 1 1 1 1 1
                2         2 2 2 2     


5                   1 2 2 2 2 2
                            3 4 
"""




