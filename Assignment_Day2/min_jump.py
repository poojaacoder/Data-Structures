def min_jumps(nums):
    n = len(nums)
    if n == 1:
        return 0
    
    jumps = 0
    farthest = 0
    current_end = 0
    
    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        print(farthest, i , current_end)
        if i == current_end:
            jumps += 1
            current_end = farthest
            if farthest >= n - 1:
                break
    
    return jumps

# Example usage:
nums1 = [2,3,1,1,4]
nums2 = [2,3,0,1,4]

print(min_jumps(nums1))  # Output: 2
print(min_jumps(nums2))  # Output: 2


# https://chatgpt.com/c/5e915089-926a-4f03-83cd-f89a52860ce0