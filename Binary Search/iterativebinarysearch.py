
def binarysearch(arr, num, left, right):
    while left <= right:
        mid = left + (right - left) //2
        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            left = mid +1
        else:
            right = mid -1
    return False
        



    

def fin_num(arr, num):
    return binarysearch(arr, num, 0, len(arr)-1)

arr = [1,2,3,4,6,7,8,9]
num = 4
print(fin_num(arr, num))
