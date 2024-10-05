import math
import heapq

class Solution:
    def network_delay_time(self, times: List[List[int]], N: int, K: int) -> int:
        
        adjacency_list = dict()
        for u, v, w in times:
            if not u in adjacency_list:
                adjacency_list[u] = []
            adjacency_list[u].append((v, w))
        
        distances = {key:math.inf for key in range(1, N + 1)}
        distances[K] = 0
        
        hq = [(distances[K], K)]
        while hq:
            (distance, v) = heapq.heappop(hq)
            
            if not v in adjacency_list:
                continue
            
            for (a,w) in adjacency_list[v]:
                candidate_distance = distances[v] + w
                
                if distances[a] > candidate_distance:
                    distances[a] = candidate_distance
                    heapq.heappush(hq, (distances[a], a))
        
        max_distance = max(distances.values())
        
        return -1 if max_distance == math.inf else max_distance
        