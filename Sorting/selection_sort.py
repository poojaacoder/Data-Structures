def selection_sort(arr):

    n = len(arr)
    for i in range(n-1):
        min =i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    print(arr)


arr =[5,40,28,7,3,2,1,10]
selection_sort(arr)

# time complexity :O(n2)
#  space complexity : 0(1)
