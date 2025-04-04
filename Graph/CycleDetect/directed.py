

def detectcycleindirectediterative(graph):

    visited = set()
    for start in graph:
        stack = []
        stack.append((start, set()))
        while stack:
            node, recstack = stack.pop()

            if node in recstack:
                return True

            if node in visited:
                continue

            visited.add(node)
            recstack.add(node)
            for n in graph.get(node, []):
                    stack.append((n, recstack))
    return False



