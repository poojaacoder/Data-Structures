class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle not in haystack:
            return -1
        if needle == haystack:
            return 0

        n = len(needle)
        firstchar = needle[0]
        for i in range(len(haystack)):
            if haystack[i] == firstchar:
                if haystack[i:i+n] == needle:
                    return i
                else:
                    i+= n            


        
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/