class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        dict_a = [0] * 26 * 2
        for val in s:
            if val.islower():
                dict_a[ord(val) - ord('a')] +=1
            if val.isupper():
                dict_a[ord(val) - ord('A')+26] +=1
        print(dict_a)

        #  unicode for a = 97
        #  unicode for A = 65
        #  for dict_a a to z would be ord(a) - ord(a)
        #  so will start a from 0 - 26
        #  and A from 27 to further
        
        odd = 0
        res = 0
        for count in dict_a:
            if count == 0:
                continue
            res += count if count % 2 == 0 else count -1
            if count % 2 == 1:
                odd = 1
        return res+odd

        # 


            


        # https://leetcode.com/problems/longest-palindrome/