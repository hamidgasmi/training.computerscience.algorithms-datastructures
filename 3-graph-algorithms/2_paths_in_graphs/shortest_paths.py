#Uses python3
import sys
import queue
from collections import namedtuple

Edge = namedtuple('Edge', ['vertex', 'weight'])

class Graph:
    def __init__(self, n, edges):
        self.adjacency_list = [[] for _ in range(n)]
        self.build_adjacency_list(edges)

    def v_size(self):
        return len(self.adjacency_list)

    def build_adjacency_list(self, edges):
        for ((s, d), w) in edges:
            self.adjacency_list[s - 1].append(Edge(d - 1, w))

    # Implementation: Bellman-Ford algorithm
    def shortest_paths(self, s, distances):
        n = self.v_size()
        parents = [-1] * n
        distances[s] = 0
        negative_cycle_reachable_nodes = []

        # Find shortest paths
        for i in range(n):
            for v in range(n):
                for a_tuple in self.adjacency_list[v]:
                    a_candidate_distance = distances[v] + a_tuple.weight
                    if distances[a_tuple.vertex] > a_candidate_distance:
                        distances[a_tuple.vertex] = a_candidate_distance
                        parents[a_tuple.vertex] = v
                        
                        if i == n - 1:
                            negative_cycle_reachable_nodes.append(a_tuple.vertex)
                            distances[s] = - 10**19
                            
        # Find all negative cycles
        visited = [False] * n
        for v in negative_cycle_reachable_nodes:
            cycle_v = self.get_cycle(v, parents)
            # Visit all nodes reachable from a negative cycle
            self.dfs(cycle_v, distances, visited)
    
    def get_cycle(self, v, parents):
        # Find a node in a cycle where v is reachable from
        cycle_v = v
        for _ in range(self.v_size()):
            cycle_v = parents[cycle_v]

        return cycle_v

        # Find all nodes of the cycle
        #cycle = []
        #cycle.append(cycle_v)
        #p = parents[cycle_v]
        #while p != cycle_v:
        #    cycle.append(p)
        #    p = parents[p]
        # return cycle

    def dfs(self, s, distances, visited):
        if visited[s]:
            return
        
        visited[s] = True
        distances[s] = - 10**19

        for a_tuple in self.adjacency_list[s]:
            self.dfs(a_tuple.vertex, distances, visited)

def shortet_paths(n, edges, s, distance):

    aGraph = Graph(n, edges)

    aGraph.shortest_paths(s, distances)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    
    s = data[0]
    s -= 1
    distances = [10**19] * n
    shortet_paths(n, edges, s, distances)
    for x in range(n):
        if distances[x] == 10**19:
            print('*')
        elif distances[x] == - 10**19:
            print('-')
        else:
            print(distances[x])
