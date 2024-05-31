class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # N = len(nums)
        # dp = [1] * N

        # for i in range(N):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp [i] = max(dp[i], dp[j]+1)
        #         print(dp)
        # return max(dp)
        # this gives O(n2) complexitty so below answer
        n = len(nums)
        dp =[nums[0]]
        for num in nums:
            x = bisect_left(dp, num)
            if x == len(dp):
                dp.append(num)
            if dp[x] > num:
                dp[x]= num
        return len(dp)

        #  above function gives ( n log n)  because bisect_left uses
        #  log n and n for one iteration
        #  0(n) space complexity
            

            # https://leetcode.com/problems/longest-increasing-subsequence/description/
    # https://www.youtube.com/watch?v=hQikNRWoTFM



# 4  10 4 3 8 9
# 1  2  1 1 2 3
        