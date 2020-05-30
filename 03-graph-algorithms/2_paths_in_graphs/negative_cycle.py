#Uses python3
import sys
from collections import namedtuple

Edge = namedtuple('Edge', ['vertex', 'weight'])

class Graph:
    def __init__(self, n, edges):
        self.adjacency_list = [[] for _ in range(n)]
        self.build_adjacency_list(edges)

    def size(self):
        return len(self.adjacency_list)

    def build_adjacency_list(self, edges):
        for ((s, d), w) in edges:
            self.adjacency_list[s - 1].append(Edge(d - 1, w))

    def bellman_ford(self):
        distances = [10**7 + 1] * self.size()
        parents = [-1] * self.size()

        distances[0] = 0

        for i in range(self.size()):
            for v in range(self.size()):
                for a in self.adjacency_list[v]:
                    a_candidate_distance = distances[v] + a.weight
                    if distances[a.vertex] > a_candidate_distance:
                        if i == self.size() - 1:
                            return 1

                        distances[a.vertex] = a_candidate_distance
                        parents[a.vertex] = v
        
        return 0

def negative_cycle(n, edges):
    
    return Graph(n, edges).bellman_ford()

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    print(negative_cycle(n, edges))
