class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        def dijakstras(start, graph):
            dist = [float('inf')] * (n+1)
            minheap = [(0, start)]
            dist[start] = 0
            while minheap:
                old_dist , node = heapq.heappop(minheap)
                if old_dist > dist[node]:
                    continue
                for neighbor, new_dist in graph.get(node, []):
                    if new_dist + old_dist < dist[neighbor]:
                        dist[neighbor] = new_dist + old_dist
                        heapq.heappush(minheap, (new_dist + old_dist, neighbor))
            
            maxdist = max(dist[1:])
            return maxdist if maxdist != float('inf') else -1

        graph = { i: [] for i in range(1,n+1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        return dijakstras(k, graph)
        
# https://leetcode.com/problems/network-delay-time/?envType=problem-list-v2&envId=graph