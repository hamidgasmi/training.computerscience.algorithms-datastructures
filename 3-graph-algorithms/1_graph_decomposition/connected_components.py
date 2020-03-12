#Uses python3
import sys

class MazeGraph:
    def __init__(self, n, edges):
        self.adj = [[] for _ in range(n)]
        self.buildAdjacencyList(edges)
        self.visited = []

    # Time Complexity: O(|E|)
    # Space Complexity: O(1)
    def buildAdjacencyList(self, edges):
        for (a, b) in edges:
            self.adj[a - 1].append(b - 1)
            self.adj[b - 1].append(a - 1)

    def isVisited(self, v):
        return self.visited[v]

    def unvisitAll(self):
        self.visited = [False] * n

    # Time Complexity: O(|E|)
    # Space Complexity: O(|V|):
    # .... Each vertex calls recursively explore method for 1 neighbor at a time
    def explore(self, v):
        self.visited[v] = True
        for a in range(len(self.adj[v])):
            if not self.isVisited(self.adj[v][a]):
                self.explore(self.adj[v][a])

    # Time Complexity: O(|V| + |E|):
    # .... Each vertex is explored exactly once
    # .... Each vertex checks each neighbor
    # Space Complexity: O(|V|):

    def DFS(self):
        self.unvisitAll()
        
        connected_components = 0
        for v in range(len(self.adj)):
            if not self.visited[v]:
                connected_components += 1
                self.explore(v)
        return connected_components

def number_of_components(n, edges):

    aMaze = MazeGraph(n, edges)

    return aMaze.DFS()

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    
    print(number_of_components(n, edges))
