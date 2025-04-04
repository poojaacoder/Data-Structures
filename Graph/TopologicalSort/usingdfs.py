
def topologicalsort(graph):
    visited = set()
    stack = []

    def dfs(start):
        visited.add(start)
        for neighbor in graph.get(start, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(start)

    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]

    
