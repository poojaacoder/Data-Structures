def findshortestpath(graph, start):
    #create distance map
    distance = {node: float('inf') for node in graph}
    #create visited set
    visited = set()
    visited.add(start)
    #create minheap
    minheap = [(0, start)] # weight, node

    while minheap:
        cur_dist, node = heapq.heappop(minheap)
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph.get(node, []):
            if neighbor in visited:
                continue
            new_dist = cur_dist + distance[neighbor]
            if distance[neighbor] > new_dist:
                distance[neighbor] = new_dist
                heapq.heappush(minheap, [new_dist, neighbor])
                print(minheap, distance)

        return distances

def findminpathforall(graph):

    shortedpathtoall = {}
    for node in graph:
        shortedpathtoall[node] = findshortestpath(graph, node)
        print(shortedpathtoall[node])
    return shortedpathtoall

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

# Example usage
start_node = 'A'
min_distances = findshortestpath(graph, start_node)
print(min_distances)

