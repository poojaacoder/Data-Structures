
def binarysearch(arr, num, left, right):
    if left > right :
        return False
    mid = left + (right-left) // 2
    if arr[mid] == num:
        return True
    if arr[mid] < num:
        return binarysearch(arr, num, mid + 1, right)
    elif arr[mid] > num:
        return binarysearch(arr, num, left, mid -1)


    

def fin_num(arr, num):
    return binarysearch(arr, num, 0, len(arr)-1)

arr = [1,2,3,4,6,7,8,9]
num = 5
print(fin_num(arr, num))
