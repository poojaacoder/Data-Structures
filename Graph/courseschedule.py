from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for des,src in prerequisites:
            graph[src].append(des)
        
        visited = set()

        for node in graph:
            stack = [(node, set())]
            while stack:
                node, recstack = stack.pop()
                if node in recstack:
                    return False
                if node in visited:
                    continue
                
                visited.add(node)
                recstack.add(node)

                for neighbor in graph.get(node, []):
                    stack.append((neighbor, recstack.copy()))
        return True
                


# https://leetcode.com/problems/course-schedule/?envType=problem-list-v2&envId=graph