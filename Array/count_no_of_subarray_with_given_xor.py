from collections import defaultdict

def subarraysWithXorK(a: [int], b: int) -> int:
    n = len(a) # size of the given array.
    xr = 0
    mpp = defaultdict(int) # declaring the dictionary.
    mpp[xr] = 1 # setting the value of 0.
    cnt = 0

    for i in range(n):
        # prefix XOR till index i:
        xr = xr ^ a[i]

        # By formula: x = xr^k:
        x = xr ^ b

        # add the occurrence of xr^k
        # to the count:
        cnt += mpp[x]

        # Insert the prefix xor till index i
        # into the dictionary:
        mpp[xr] += 1

    return cnt

