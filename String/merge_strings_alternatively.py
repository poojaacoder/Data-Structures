class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length_one = len(word1)
        length_two = len(word2)

        result = ''
        min = length_one if length_one < length_two else length_two
        max = length_one if length_one > length_two else length_two
        max_number = word1 if length_one > length_two else word2
        for i in range(min):
            result += word1[i]
            result += word2[i]
        if length_one  != length_two:
            print(length_one, length_two)
            print(max-min, len(max_number))
            result +=  max_number[min:len(max_number)]
        
        return result


        # https://leetcode.com/problems/merge-strings-alternately/description/