class Solution:
    def maxArea(self, height: List[int]) -> int:

        start = 0
        end = len(height)-1
        max_area = 0
        while start < end:
            max_area = max(max_area, ((end-start)* min(height[end],height[start])))
            if height[start] > height[end]:
                end -=1
            else:
                start +=1
        return max_area



# https://leetcode.com/problems/container-with-most-water/