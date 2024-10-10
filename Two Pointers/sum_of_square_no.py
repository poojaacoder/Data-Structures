class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False
        start = 0
        end = int(math.sqrt(c))

        while start <= end:
            summ = (start * start) + (end * end)
            if summ == c:
                return True
            if summ > c:
                end -=1
            if summ < c:
                start +=1
        return False



            




        # https://leetcode.com/problems/sum-of-square-numbers/description/