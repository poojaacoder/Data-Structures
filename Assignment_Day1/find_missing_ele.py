# Function to find the missing element
def getMissingNo(arr, n):
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(arr)
    return total - sum_of_A

# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 5]
    N = len(arr)
    
    # Function call
    miss = getMissingNo(arr, N)
    print(miss)
    
