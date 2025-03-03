
# class Node:
#     def __init__(self, val, neigbours=None):
#         self.val = val
#         self.neigbours = neigbours

"""
input : [1, 3], [3,5], [6, 8], n = 7
"""

from collections import defaultdict
def convertlisttomatrix(edges, n):
    matrix = [[0] * (n+1) for _ in range(n+1)]

    
    for u, v in edges:
        print(u,v)
        matrix[u][v] = 1
        matrix[v][u] = 1
    return matrix

def convertlisttomatrixweighted(edges, n):
    matrix = [[0] * (n+1) for _ in range(n+1)]

    
    for u, v, w in edges:
        matrix[u][v] = w
    return matrix


def convertlisttoadj(edges):
    dicta = defaultdict(list)
    for u, v in edges:
        print(u, v)
        dicta[u].append(v)
        dicta[v].append(u)
    return dicta

def convertlisttoadjweighted(edges):
    dicta = defaultdict(list)
    for u, v , w in edges:
        dicta[u].append([v,w])
    return dicta


edges =[[1, 3], [3,5], [6, 8], [7,5]]
weighted_list = [[1, 3, 10], [3,5, 5], [6, 8, 2], [7,5, 9]]
n = 8
# print(convertlisttoadj(edges))
# print(convertlisttomatrix(edges, n))
# print(convertlisttomatrixweighted(weighted_list, n))
print(convertlisttoadjweighted(weighted_list))




    


