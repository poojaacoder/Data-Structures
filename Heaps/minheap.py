import heapq

def getMin(arr):
    heapq.heapify(arr)
    heapq.heappush(arr, 5)

    
    print("printing min")
    for i in range(len(arr)):
        min = heapq.heappop(arr)
        print(min)

arr = [10, 24, 38, 19, 8, 9]
getMin(arr)

