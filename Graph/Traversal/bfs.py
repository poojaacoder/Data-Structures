
from collections import deque
def bfs(graph, start):
    visited = set()
    q = deque()
    q.append(start)
    visited.add(start)
    
    bfs_traversal = []

    while q:
        node = q.popleft()
        bfs_traversal.append(node)
        for neighbor in graph.get(node,[]):
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
    return bfs_traversal




def bfslevels(graph, start):
    visited = set()
    q = deque()
    q.append(start)
    visited.add(start)
    bfslevels = [[start]]

    while q:
        levels = []
        node = q.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
                levels.append(neighbor)
        if levels:
            bfslevels.append(levels)
    return bfslevels


def find_path(graph, start, n):
    levels = bfslevels(graph, start)
    nodes = [float('inf')] * n
    for ind in range(1, len(levels)):
        for node in levels[ind]:
            nodes[node]= ind
    return nodes


# 






    


    


    


dfslist = {1: [3], 3: [1, 5], 5: [3, 7, 8], 6: [8], 8: [6, 9, 10], 7: [5], 11:[20]}
print(bfs(dfslist, 1))
# print(bfslevels(dfslist, 1))
