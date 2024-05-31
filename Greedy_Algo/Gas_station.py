
def canCompleteCircuit(gas, cost):

    if sum(gas) < sum(cost):
        return -1
    left = 0
    start = 0
    for i in range(len(gas)):
        left += (gas[i]-cost[i])
        if left < 0:
            left = 0
            start = i+1 
            print(start)

    return start


gas = [1,2,3,4,5]
cost =[3,4,5,1,2]
print(canCompleteCircuit(gas, cost))

# https://leetcode.com/problems/gas-station/
# https://www.youtube.com/watch?v=lJwbPZGo05A