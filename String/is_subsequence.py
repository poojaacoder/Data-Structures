class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        substring = s
        start = 0
        for ch in t:
            if start == len(s):
                break
            if ch == substring[start]:
                start +=1
        return start == len(s)


        # https://leetcode.com/problems/is-subsequence/description/