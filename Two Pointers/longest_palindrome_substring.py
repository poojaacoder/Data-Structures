class Solution:
    def longestPalindrome(self, s: str) -> str:

        # if len(s) == 1:
        #     return s[0]
        # def ispalindrome(start, end):
        #     word = s[start:end+1]
        #     while start <= end:
        #         if s[start] != s[end]:
        #             return False
        #         start +=1
        #         end -=1
        #     return True

        # max_len = 1
        # max_substring = s[0]
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)):
        #         if ispalindrome(i, j):
        #             cur_len = j - i +1
        #             if cur_len > max_len:
        #                 max_len = cur_len
        #                 max_substring = s[i:j+1]
        # return max_substring
        if len(s) == 0:
            return ""

        def expand_palindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right +=1
            return s[left+1:right]
        
        longest_substring = ""
        for i in range(len(s)):

            odd_substring = expand_palindrome(i, i)
            if len(odd_substring) > len(longest_substring):
                longest_substring = odd_substring
 
            even_palindrome = expand_palindrome(i, i+1)
            if len(even_palindrome) > len(longest_substring):
                longest_substring = even_palindrome
        
        return longest_substring


# https://leetcode.com/problems/longest-palindromic-substring/