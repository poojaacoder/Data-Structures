
def topological_sort(graph):
    visited = set()
    stack = []
        def dfs(node):
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(neighbor)
        for node in graph:
            if node not in visited:
                dfs(node)
        return stack[::-1]

