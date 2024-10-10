from collections import defaultdict 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # ransomNote_dict = defaultdict()
        # magazine_dict = defaultdict()

        # for ch in ransomNote:
        #     ransomNote_dict[ch] = ransomNote_dict.get(ch, 0) +1

        # for ch in magazine:
        #     magazine_dict[ch] = magazine_dict.get(ch, 0) +1

        # for key in ransomNote_dict.keys():
        #     if key not in magazine_dict:
        #         return False
        #     if ransomNote_dict[key] > magazine_dict[key]:
        #         return False
        # return True

        magzine_dict = [0] * 26
        ransom_dict = [0] * 26

        for ch in magazine:
            magzine_dict[ord(ch)-ord('a')] +=1
        for ch in ransomNote:
            ransom_dict[ord(ch)-ord('a')]+=1

        for ch in ransomNote:
            if ransom_dict[ord(ch)-ord('a')] > magzine_dict[ord(ch)-ord('a')]:
                return False
        return True

            
        # https://leetcode.com/problems/ransom-note/