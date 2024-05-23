def find_profit(prices):
    min_price= prices[0]
    max_profit = 0

    for  i in  range(1,len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]

        max_profit = max(max_profit, prices[i]- min_price)
    return max_profit


print(find_profit([7,1,2,3,4,5,6]))