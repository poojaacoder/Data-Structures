# Brute Force and binary search 

def aggresive_cows(dist, stalls, k):
    cows_count = 1
    prev = stalls[0]
    for n in range(1, len(stalls)-1):
        if stalls[n] - prev >= dist:
            cows_count +=1
            prev = stalls[n]
        if cows_count == k:
            return True
    return False

def findminmax(stalls, k):
    stalls.sort()
    limit = stalls[n-1] -stalls[0]
    #for ind in range(1, limit):
    #    if not aggresssive_cows(ind, stalls, k):
    #        return ind + 
    left = 1
    right = limit
    while left < right:
        mid = left + (right - left) //2
        if aggresive_cows(mid, stalls, k):
            right  = mid
        else:
            left = mid+ 1
    return left
            
    

    