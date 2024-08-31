from typing import List
import collections
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, des = edges[i]
            adj[src].append((des, succProb[i]))
            adj[des].append((src, succProb[i]))

        visit = set()
        pq = [(-1, start_node)]
        while pq:
            prob, cur = heapq.headpop(pq)
            visit.add(cur)
            if cur == end_node:
                return -1 * prob
            for edge_node, edgeProb in adj[cur]:
                if edge_node not in visit:
                    heapq.heappush(pq, (edgeProb*prob, edge_node))
        return 0
