# https://leetcode.com/problems/house-robber/description/
# https://leetcode.com/problems/house-robber/solutions/156523/From-good-to-great.-How-to-approach-most-of-DP-problems/

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = prev2 = 0
        for n in nums:
            temp = max(n+ prev1, prev2)
            prev1 = prev2
            prev2 = temp
        return prev2





        

