class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create ajgraph
        graph = defaultdict(list)
        indegree = indegree = {i: 0 for i in range(numCourses)} 
        for des, start in prerequisites:
            graph[start].append(des)
            indegree[des] +=1


        # copy all 0 degree to q
        q = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)

        # add order and decrese the indegree of nodes
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for neighbor in graph.get(node, []):
                indegree[neighbor] -=1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # return
        if len(order) == numCourses:
            return order
        else:
            return []

# https://leetcode.com/problems/course-schedule-ii/?envType=problem-list-v2&envId=graph