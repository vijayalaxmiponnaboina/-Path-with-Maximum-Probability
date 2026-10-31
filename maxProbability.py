import heapq
class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        adj=[]
        for i in range(n):
            adj.append([])
        for i,(u,v) in enumerate(edges):
            p=succProb[i]
            adj[u].append((v,p))
            adj[v].append((u,p))
        dist=[0.0]*n
        dist[start_node]=1.0
        min_heap=[(-1.0,start_node)]
        while min_heap:
            curr_prob,node=heapq.heappop(min_heap)
            if -(curr_prob) < dist[node]:
                continue
            for ne,p in adj[node]:
                new_prob=-(curr_prob)*p
                if new_prob > dist[ne]:
                    dist[ne]=new_prob
                    heapq.heappush(min_heap,(-new_prob,ne))
        return dist[end_node]