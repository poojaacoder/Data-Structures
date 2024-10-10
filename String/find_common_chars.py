class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        final_count = [float('inf')] * 26

        for word in words:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            for i in range(26):
                final_count[i] = min(final_count[i], count[i])

        for i in range(26):
            for j in range(final_count[i]):
                ans.append(chr(i + ord('a')))
        print(ans)
        return ans

       

        # https://leetcode.com/problems/find-common-characters/description/