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
    def bfs(self):

        color = [-1] * len(self.adj)
        color[0] = 0

        q = queue.Queue()
        q.put(0)
        while not q.empty():
            v = q.get()
            otherColor = 0 if color[v] == 1 else 1
            for a in self.adj[v]:
                if color[a] == -1:
                    color[a] = otherColor
                    q.put(a)
                elif color[a] == color[v]:
                    return 0

        return 1


def bipartite(n, edges):
    aGraph = Graph(n, edges)
    
    return aGraph.bfs()

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    print(bipartite(n, edges))