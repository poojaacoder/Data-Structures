class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for passengers, start , end in trips:
            heapq.heappush(events, (start, passengers ))
            heapq.heappush(events, (end, -passengers ))

        cur_passengers = 0

        while events:
            _, passengers = heapq.heappop(events)
            cur_passengers += passengers

            if cur_passengers > capacity:
                return False
        
        return True
        

        # https://leetcode.com/problems/car-pooling/?envType=problem-list-v2&envId=heap-priority-queue