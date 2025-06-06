


def detect_cycle_multiple_components(graph):
    visited = set()
    def detect_cycle(graph , node, parent):
        visited.add(node)
        for n in graph.get(node, []):
            if n not in visited:
                if detect_cycle(graph, n, node):
                    return True
            elif n != parent:
                return True
        return False
    
    for node in graph:
        if node not in visited:
            if detect_cycle(graph, node, visited):
                return True
    return False

def detectcycleundirectediterative(graph):
    visited = set()
    for start in graph:
        if start not in visited:
            stack = []
            stack.append((start, None))
            while stack:
                node, parent = stack.pop()

                if node in visited:
                    continue
                visited.add(node)

                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        stack.append((neighbor, node))
                    elif neighbor != parent:
                        return True
    return False




def cycle_detect(graph):
    visited = set()
    for key in graph.keys():
        if key in visited:
            continue
        if dfs(graph, key, -1, visited):
            return True
    return False



# recursive_helper
def dfs_recursive(graph, node, parent, visited):
    if node in visited:
        return True
    visited.add(node)
    for neighbor in graph.get(node, []):
        if dfs_recursive(graph, neighbor, node, visited):
            return True
        elif neighbor != parent:
            return True
    return False


# iterative_helper
def dfs(graph, node, parent, visited):

    visited.add(node)
    stack = []
    stack.append([node, parent])
    while stack:
        node, parent = stack.pop()
        for neighbor in graph.get(node, []):
            if neighbor == parent:
                continue
            if neighbor in visited:
                return True
            stack.append([neighbor, node])
            visited.add(neighbor)
    return False





    


    
















cycledfslist = {1: [3], 3: [1, 5], 5: [3, 7], 6: [8], 8: [6], 7: [5, 1]}
no_cyclelist = {1: [3], 3: [5], 5: [ 7], 6: [8], 8: [7]}
third_list = { 1: [2], 2: [1]}

# print(detect_cycle(cycledfslist,1))

# print(detect_cycle(no_cyclelist,1))


# print(detect_cycle_multiple_components(no_cyclelist))
# print(detect_cycle(third_list,1))
# print(cycle_detect(cycledfslist))
# print(cycle_detect(cycledfslist))
print(cycle_detect(cycledfslist))