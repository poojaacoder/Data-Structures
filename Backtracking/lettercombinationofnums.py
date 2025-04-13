class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        if digits == "":
            return []

        def cal(ind, arr):
            if ind == len(digits):
                ans.append(arr)
                return 
            word = mp[digits[ind]]
            for ch in word:
                cal(ind+1, arr+ch)
        ans = []
        cal(0, '')
        return ans
                
        

        # https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=problem-list-v2&envId=backtracking