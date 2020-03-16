#Uses python3
import sys
import queue

class Graph:
    def __init__(self, n, edges):
        self.adj = [[] for _ in range(n)]
        self.buildAdjacencyList(edges)

    # Time Complexity: O(|E|)
    # Space Complexity: O(1)
    def buildAdjacencyList(self, edges):
        for (a, b) in edges:
            self.adj[a - 1].append(b - 1)
            self.adj[b - 1].append(a - 1)

    # Time Complexity: O(|V| + |E|)
    # Space Complexity: O(|V|)
    def bfs(self, s, t):

        if s == t:
            return 0

        distance = [-1] * len(self.adj)
        
        q = queue.Queue()
        q.put(s)
        distance[s] = 0
        while not q.empty():
            v = q.get()

            for a in self.adj[v]:
                if distance[a] == -1:
                    distance[a] = distance[v] + 1
                    q.put(a)
                    if a == t:
                        return distance[a]

        return distance[t]

def distance(n, edges, s, t):
    
    aGraph = Graph(n, edges)
    
    return aGraph.bfs(s, t)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(n, edges, s, t))
