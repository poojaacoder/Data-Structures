class Solution:
    def reverseWords(self, s: str) -> str:

        ans = []
        """

        " the sky is blue "
        """
        res = ''
        start = end = len(s)-1
        while start >= 0:
            if s[end] == ' ':
                start -=1
                end -=1
            elif s[start] != ' ':
                start -=1
            else:
                word = s[start+1:end+1]
                res += word +' '
                end = start
        
        if s[start+1:end+1] != ' ' and end >=0:
            res += s[start+1:end+1]
        return res.rstrip()


            



        # https://leetcode.com/problems/reverse-words-in-a-string/