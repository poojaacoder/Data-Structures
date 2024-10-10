# https://www.youtube.com/watch?v=2VLwjvODQbA
# https://leetcode.com/problems/meeting-rooms-iii/description/

import heapq
def meetingRooms(n, meetings):
    meetings.sort()
    available = [i for i in range(n)]
    busy = [] #(end_time, room)
    count = [0] *n


    for start , end in meetings:
        while busy and busy[0][0] <= start:
            _, room = heapq.heappop(busy)
            heapq.heappush(available, room)
        if available:
            room = heapq.heappop(available)
            heapq.heappush(busy, (end, room))
        else:
            end_time, room = heapq.heappop(busy)
            end = end_time + (end - start)
            heapq.heappush(busy, (end, room)) 
        count[room] +=1

    return count.index(max(count))

meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
rooms = 2

print(meetingRooms(rooms, meetings))

