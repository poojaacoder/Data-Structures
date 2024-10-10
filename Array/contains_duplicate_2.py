class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for key, value in enumerate(nums):
            if value in index_map:
                if key - index_map[value]  <= k:
                    return True
            index_map[value] = key
        return False



# https://leetcode.com/problems/contains-duplicate-ii/