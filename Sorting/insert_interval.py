class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        intervals.sort()

        for i in range(len(intervals)):
            # 1. if new sits at first
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            # 2. if it does not sit , just add cur to list
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            #  3. if its overlapping , merge it and then dont add it, beacuse we will be checking 
            # further intervals 
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1],intervals[i][1])]

        res.append(newInterval)
        return res
    


    # https://leetcode.com/problems/insert-interval/