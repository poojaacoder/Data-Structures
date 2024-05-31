class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        result = 0

        for num in nums:
            if count == 0:
                result= num
            if result == num:
                count +=1
            else:
                count -=1

        return result

        # https://www.youtube.com/watch?v=7pnhv842keE
    # https://leetcode.com/problems/majority-element/submissions/1265921292/