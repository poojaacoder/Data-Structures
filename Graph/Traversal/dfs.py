
from collections import defaultdict
def converttoadj(edges):
    dicta = defaultdict(list)
    for u , v in edges:
        dicta[u].append(v)
        dicta[v].append(u)
    return dicta

# recursive
def dfs(dfslist, start, visited):
    if start in visited:
        return
    visited.append(start)
    for neighbor in dfslist[start]:
        if neighbor not in visited:
            dfs(dfslist, neighbor, visited)


    
# iterative
def dfsIterative(dfslist, start):
    stack = [start]
    visited = set()
    res = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        res.append(node)
        for neighbor in reversed(dfslist[node]):
            if neighbor not in visited:
                stack.append(neighbor)
    return res

    



edges =[[1, 3], [3,5],[6, 8],[7,5]]
weighted_list = [[1, 3, 10], [3,5, 5], [6, 8, 2], [7,5, 9]]
dfslist = {1: [3], 3: [1, 5], 5: [3, 7], 6: [8], 8: [6], 7: [5]}
n = 8

visitied = []
# dfs(dfslist, 1, visitied)
print("recursive", visitied)
print(dfsIterative(dfslist, 1))


