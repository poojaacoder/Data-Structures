class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
            
        
        def _dijkstra(graph, src, dst, k):
            dist = [[math.inf] * (k + 2) for _ in range(len(graph))]

            dist[src][k + 1] = 0
            minHeap = [(dist[src][k + 1], src, k + 1)]

            while minHeap:
                d, u, stops = heapq.heappop(minHeap)
                if u == dst:
                    return d
                if stops == 0 or d > dist[u][stops]:
                    continue
                for v, w in graph[u]:
                    if d + w < dist[v][stops - 1]:
                        dist[v][stops - 1] = d + w
                        heapq.heappush(minHeap, (dist[v][stops - 1], v, stops - 1))

            return -1
        

        graph = [[] for _ in range(n)]

        for u, v, w in flights:
            graph[u].append((v, w))

        return _dijkstra(graph, src, dst, k)
    

    # https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/1581008938/?envType=problem-list-v2&envId=graph