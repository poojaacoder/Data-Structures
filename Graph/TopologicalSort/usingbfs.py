
from collections import defaultdict, deque
def topologicalsort(graph):
    # create in degree
    indegree = defaultdict(int)
    for node in graph:
        for neighbor in graph.get(node, []):
            indegree[neighbor] +=1

    # copy all 0 in queue
    queue = deque()
    for node in indegree:
        if indegree[node] == 0:
            queue.append(node)


    # traverse and store in queue, while adding to order
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for node in graph:
            for neighbor in graph.get(node, []):
                indegree[neighbor] -=1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
   


    # if len order is less than then its a cycle
    if len(order) == len(graph):
        return order
    else:
        print("cycle detected")
        return []

