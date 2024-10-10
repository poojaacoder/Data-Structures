class Solution:
    def isHappy(self, n: int) -> bool:
        def numsqaure(n):
            num = 0
            while n:
                digit = n % 10
                num = num + digit * digit
                n = n // 10
            return num
        
        set_a = set()
        while 1:
            n = numsqaure(n)
            if n == 1:
                return True
            if n in set_a:
                return False
            set_a.add(n)

# https://leetcode.com/problems/happy-number/