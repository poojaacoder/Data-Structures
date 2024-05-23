
def two_sum(nums, target):
    dict_num = {}

    for index, num in enumerate(nums):
        dict_num[num] = index

    for index, num in enumerate(nums):
        if (target - num) in dict_num and index != dict_num[target-num]:
            return [index, dict_num[target-num]]

print(two_sum([1,3,2,7,5,11],9))