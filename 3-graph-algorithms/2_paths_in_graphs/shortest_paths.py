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
    def shortest_paths(self, s, distances, reachable, shortest):
        n = self.v_size()
        parents = [-1] * n
        
        distances[s] = 0
        reachable[s] = 1
        
        q = queue.Queue()

        # Find shortest paths
        for i in range(n):
            for v in range(n):
                if distances[v] != 10**19:
                    for a_tuple in self.adjacency_list[v]:
                        a_candidate_distance = distances[v] + a_tuple.weight
                        if distances[a_tuple.vertex] > a_candidate_distance:
                            distances[a_tuple.vertex] = a_candidate_distance
                            parents[a_tuple.vertex] = v
                            reachable[a_tuple.vertex] = 1
                            if i == n - 1:
                                q.put(a_tuple.vertex)
                            
        # Find all negative cycles (BFS traversal)
        visited = [False] * n
        self.bfs(q, shortest, visited)
            
    def bfs(self, q, shortest, visited):
        while not q.empty():
            v = q.get()
            visited[v] = True
            shortest[v] = 0
            for a_tuple in self.adjacency_list[v]:
                if not visited[a_tuple.vertex]:
                    q.put(a_tuple.vertex)

def shortet_paths(n, edges, s, distances, reachable, shortest):

    aGraph = Graph(n, edges)

    aGraph.shortest_paths(s, distances, reachable, shortest)

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
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(n, edges, s, distances, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print("*")
        elif shortest[x] == 0:
            print("-")
        else:
            print(distances[x])
