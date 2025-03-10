class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def isenough(num):
            count = 0
            for val in range(1, m+ 1):
                add = min(num//val, n)
                if add == 0:
                    break
                count += add
            return count >= k
        
        left = 1
        right = m * n
        while left < right:
            mid = left + (right - left) //2
            if isenough(mid):
                right = mid
            else:
                left = mid + 1
        return left 
        