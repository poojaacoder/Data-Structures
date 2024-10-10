def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = ""
    for chars in zip(*strs):
        print(chars)
        if len(set(chars)) == 1:
            prefix += chars[0]
        else:
            break
    return prefix

strs = ["flower","flower","flower"]
print(longest_common_prefix(strs))

def zipp():
    arr1 = [1,2,3,4,5]
    arr2 = [1,2,3,4,5]
    print([x for x in zip(arr1, arr2)])

zipp()