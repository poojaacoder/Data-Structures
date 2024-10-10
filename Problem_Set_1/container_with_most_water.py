class Solution:
    def maxArea(self, height) -> int:
        result = 0
        left = 0
        right = len(height)-1
        while left <= right:
            area = (right- left) * min(height[left], height[right])
            result = max(result, area)

            if height[left] > height[right]:
                right -=1
            else:
                left +=1
        return result
        

# https://leetcode.com/problems/container-with-most-water/description/