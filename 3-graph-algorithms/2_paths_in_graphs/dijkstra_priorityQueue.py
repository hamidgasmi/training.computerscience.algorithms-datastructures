import sys
import queue
from collections import namedtuple

Edge = namedtuple('Edge', ['vertex', 'weight'])

class Graph:
    def __init__(self, n, edges):
        self.adjacency_list = [[] for _ in range(n)]
        self.build_adjacency_list(n, edges)

    def build_adjacency_list(self, n, edges):
        for ((s, d), w) in edges:
            self.adjacency_list[s - 1].append(Edge(d - 1, w))

    # Implementation: Binary Heap
    # ... The number of flight ~ the number of cities => |V| ~ |E| => Sparse Graph => Binary Heap is more efficient
    # ... T(n) = O((|V| + |E|) log |V|)
    def dijkstra(self, s, t):
        
        # w <= 10^3 and |V| <= 10^4
        # Shortest Path Cost <= 10^3 * 10^4 + 1
        distances = [10**7 + 1] * len(self.adjacency_list)
        distances[s] = 0
        
        parents = [None] * len(self.adjacency_list)
        parents[s] = -1

        q = queue.PriorityQueue()
        for v in range(0, len(self.adjacency_list)):
            if v == s:
                continue
            q.put([distances[v], v])
        q.put([distances[s], s])

        while not q.empty():
            v_min_weight = q.get()
            v = v_min_weight[1]

            if v == t:
                return distances[t]
            
            for a_tuple in self.adjacency_list[v]:
                a_candidate_distance = distances[v] + a_tuple.weight
                if distances[a_tuple.vertex] > a_candidate_distance:
                    distances[a_tuple.vertex] = a_candidate_distance
                    parents[a_tuple.vertex] = v
                    q.put([distances[a_tuple.vertex], a_tuple.vertex])

        return distances[t]

def distance(n, edges, s, t):

    aFlightNetwork = Graph(n, edges)
    distance = aFlightNetwork.dijkstra(s, t) 
    return -1 if distance == 10**7 + 1 else distance

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    s, t = data[0] - 1, data[1] - 1
    print(distance(n, edges, s, t))
