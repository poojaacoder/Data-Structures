

arr = [
    [0,0,0,0,5],
    [0,1,1,1,0],
    [2,0,0,0,0]

]

# [[2, 0, 0, 0, 5],
#   [2, 0, 0, 0, 5],
#     [2, 0, 0, 0, 5]]

# i  
# [0, 2, 2, 7, 1],
# [0, 2, 2, 7, 1],
# [0, 2, 2, 7, 1]


def findpath(grid):
    rows = len(grid)
    cols = len(grid[0])

    dp = [[0] * cols for i in range(rows)]
    # update last row

    #  update start point
    dp[rows-1][0] = grid[rows-1][0]
    print(dp)



    # update first column
    for i in range(rows-2, -1, -1):
        dp[i][0]= dp[i][0] + dp[i+1][0]

        # update last rows
    for j in range(1,cols):
        dp[rows-1][j] = grid[rows-1][j]+ grid[rows-1][j-1]

    # update rest cols and rows
    for i in range(rows-2,-1 ,-1):
        for j in range(1, cols):
            dp[i][j] += max(dp[i+1][j], dp[i][j-1])+ grid[i][j]

    print(dp)
    return dp[0][cols-1]

print(findpath(arr))