
from collections import defaultdict, deque
def topologicalsort(graph): 
#   create indegree
    indegree = defaultdict(int)
    for node in graph:
        for neighbor in graph.get(node, []): 
            indegree[neighbor]+=1
    
    for node in graph:
        indegree[node] += 0  
# copy ele with 0 degree to q
    q = deque()
    for node in graph:
        if indegree[node] == 0:
            q.append(node)
#  main execution to free the degrees
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            indegree[neighbor] -=1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    if len(order) == len(graph):
        return order
    else:
        print('cycle detected')

    
# 
