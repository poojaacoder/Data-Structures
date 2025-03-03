
def topologicalsort(graph):
    visited = set()
    stack = []

    def dfs(start):
        visited.add(start)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]

    
