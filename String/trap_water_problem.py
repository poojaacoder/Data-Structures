
def trap (height):
    n = len(height)

    if n < 1:
        return 0
    
    ans = 0
    left_max = [0] *n
    right_max = [0] * n

    left_max[0] = height [0]
    for i in range(1,n):
        left_max[i] = max(left_max[i-1], height[i])

    right_max[-1] = height[-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    

    for i in range(n):
        ans += min(left_max[i], right_max[i])- height[i]

    return ans

h = [0,1,0,2,1,0,1,3,2,1,2,1]
h2 = [4,2,0,3,2,5]
print(trap(h))
print(trap(h2))