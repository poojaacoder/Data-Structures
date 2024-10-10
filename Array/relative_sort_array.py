class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """

        """
        count_map = [0] * 1001
        result = []

        for n in arr1:
            count_map[n] +=1
        
        for n in arr2:
            while count_map[n] > 0:
                result.append(n)
                count_map[n] -=1

        for n in range(1001):
            for _ in range(count_map[n]):
                result.append(n)

        return result

        # https://leetcode.com/problems/relative-sort-array/