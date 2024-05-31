class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for entry in sorted(intervals):
            if not result or result[-1][1] < entry[0]:
                result.append(entry)
            else:
                result[-1][1] = max(result[-1][1], entry[1])
        return result


        