def two_sum(arr, target):

    dict_num = {}
    for index, num in enumerate(arr):
        dict_num[num] = index

    for index, num in enumerate(arr):
        if (target- num) in dict_num and index != dict_num[target-num]:
            return [index, dict_num[target-num]]
        else:
            return []