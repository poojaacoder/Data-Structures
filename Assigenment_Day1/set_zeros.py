def set_zeros(matrix):
    zeros_col = set()
    zeros_row = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zeros_row.add(i)
                zeros_col.add(j)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in zeros_row or j in zeros_col:
                matrix[i][j] = 0

matrix = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]

set_zeros(matrix)

# Output the modified matrix
for row in matrix:
    print(row)


    # time complexity : O(n)*

