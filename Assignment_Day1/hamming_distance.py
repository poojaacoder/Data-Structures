def totalHammingDistance(nums) -> int:
    def hamming_distance(x, y):
        num = x ^ y
        num = format(num, 'b')
        count = 0
        for i in num:
            count += int(i)
        return count

    sum = 0
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            sum += hamming_distance(nums[i], nums[j])

    return sum


k = [4,14,2]
print(totalHammingDistance(k))