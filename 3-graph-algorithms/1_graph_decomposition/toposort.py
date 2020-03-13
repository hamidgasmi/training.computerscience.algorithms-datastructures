#Uses python3
import sys

class Graph:
    def __init__(self, n, edges):
        self.adj = [[] for _ in range(n)]
        self.buildAdjacencyList(edges)
    
    # Time Complexity: O(|E|)
    # Space Complexity: O(1)
    def buildAdjacencyList(self, edges):
        self.reset()

        for (a, b) in edges:
            self.adj[a - 1].append(b - 1)

    def reset(self):
        self.visited = [False] * len(self.adj)
        self.removed = [False] * len(self.adj)

    def explore(self, v, order):
        self.visited[v] = True
        for a in self.adj[v]:
            if not self.removed[a]:
                self.explore(a, order)
        
        self.removed[v] = True
        order.append(v)

    def dfs(self, order):
        self.reset()
        for v in range(len(self.adj)):
            if not self.removed[v]:
                self.explore(v, order)

    def toposort(self):
        order = []
        self.dfs(order)
        return order[::-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    
    aGraph = Graph(n, edges)
    order = aGraph.toposort()
    for x in order:
        print(x + 1, end=' ')

