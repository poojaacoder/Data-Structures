# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
def minDays( bloomDay, m :int, k: int) -> int:
    n = len(bloomDay)
    if n < m* k:
        return -1
    
    def make_bouquet(days):
        bouquet_count = bloomed_flowers =0
        for flower in bloomDay:
            if flower <= days:
                bloomed_flowers +=1
            else:
                bloomed_flowers = 0

            if bloomed_flowers >= k:
                bouquet_count+=1
                bloomed_flowers =0
        return bouquet_count >=  m
    
    left = min(bloomDay)
    right = max (bloomDay)
    while left < right:
        mid = (left + right ) //2

        if make_bouquet(mid):
            right = mid
        else:
            left = mid + 1
    return left




bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(minDays(bloomDay, m ,k))