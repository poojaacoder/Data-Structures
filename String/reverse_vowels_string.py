class Solution:
    def isvowel(self, c):
        if (c == 'a' or c == 'A' or c == 'e' or
        c == 'E' or c == 'i' or c == 'I' or
        c == 'o' or c == 'O' or c == 'u' or c == 'U'):
            return True
        return False

    def reverseVowels(self, s: str) -> str:
        j = 0 
        vowel = [0] * len(s)
        stra = list(s)

        for i in range(len(stra)):
            if self.isvowel(stra[i]):
                vowel[j] = stra[i]
                j += 1
            
        print(j)
        for i in range(len(stra)):
            if self.isvowel(stra[i]):
                j -= 1
                stra[i] = vowel[j]
        
        k = ''.join(stra)
        return k


        
        # https://leetcode.com/problems/reverse-vowels-of-a-string/