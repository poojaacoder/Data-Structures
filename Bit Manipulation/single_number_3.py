import functools , operator
def singleNumber(nums):
    xors = functools.reduce(operator.xor, nums)
    lowbit = xors & -xors
    ans = [0, 0]

    # Seperate `nums` into two groups by `lowbit`.
    for num in nums:
        if num & lowbit:
            ans[0] ^= num
        else:
            ans[1] ^= num

    return ans


k = [2, 3, 1, 2, 4 , 3]
print()