def bubble_sort(arr):

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]  = arr[j+1], arr[j]
        
    print(arr)

arr =[5,40,28,7,3,2,1,10]
bubble_sort(arr)

# time complexity :O(n2)
#  space complexity : 0(1)
