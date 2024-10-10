def count_no_of_subarray(arr,k):
    prefix = [0] * (len(arr)+1)
    count , odd = 0, 0

    for i in range(len(arr)):
        prefix[odd]+=1

        if arr[i] & 1:
            odd +=1
        if odd >= k:
            count += prefix[odd - k]
        print(prefix)
    return count

arr = [1,1,2,1,1]
arr2 = [2,2,2,1,2,2,1,2,2,2]
k = 3
k2 = 2
print(count_no_of_subarray(arr2, k2))