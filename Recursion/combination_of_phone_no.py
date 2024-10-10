class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
    
        mp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def combine(ind, path):
            nonlocal res
            if ind == len(digits):
                res.append(''.join(path))
                return 
            word = mp[digits[ind]]
            for letter in word:
                path.append(letter)
                combine(ind+1, path)
                path.pop()
            

        res = []
        combine(0, [])
        return res

        """

        a , b , c from 0 
        d e f to next index
        """
        
        # https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/