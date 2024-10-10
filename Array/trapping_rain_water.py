class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_height = [0] * n
        right_height = [0] * n
        res = 0

        left_height[0] = height[0]
        right_height[-1] = height[-1]

        for i in range(1, len(height)):
            left_height[i] = max(left_height[i-1], height[i])

        for i in range(len(height)-2, -1, -1):
            right_height[i] = max(right_height[i+1], height[i])
        
        for i in range(len(height)):
            res += min(left_height[i], right_height[i]) - height[i]
        
        return res

    

        

# https://leetcode.com/problems/trapping-rain-water/