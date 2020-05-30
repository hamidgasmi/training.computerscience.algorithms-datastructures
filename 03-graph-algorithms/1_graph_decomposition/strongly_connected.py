import sys

sys.setrecursionlimit(200000)

class Graph:
    def __init__(self, n, edges):
        self.visited = [False] * n
        self.adj = [[] for _ in range(n)]
        self.adjReverse = [[] for _ in range(n)]
        self.buildAdjacencyList(edges)
        
    # Time Complexity: O(|E|)
    # Space Complexity: O(1)
    def buildAdjacencyList(self, edges):
        for (a, b) in edges:
            self.adj[a - 1].append(b - 1)
            self.adjReverse[b - 1].append(a - 1)

    def explore(self, v, adj, postOrderVisits):
        self.visited[v] = True
        for a in adj[v]:
            if not self.visited[a]:
                self.explore(a, adj, postOrderVisits)

        postOrderVisits.append(v)

    def dfs(self, adj, postOrderVisits):
        self.visited = [False] * n
        for v in range(len(adj)):
            if not self.visited[v]:
                self.explore(v, adj, postOrderVisits)

    def number_of_strongly_connected_components(self):
        
        postOrderVisits = []
        self.dfs(self.adjReverse, postOrderVisits)
        self.visited = [False] * n
        aSCCList = []
        for i in range(len(postOrderVisits) - 1, -1, -1):
            v = postOrderVisits[i]
            if not self.visited[v]:
                aSCC = []
                self.explore(v, self.adj, aSCC)
                aSCCList.append(aSCC)

        return aSCCList

def number_of_strongly_connected_components(n, edges):
    aGraph = Graph(n, edges=edges)

    return len(aGraph.number_of_strongly_connected_components())

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    print(number_of_strongly_connected_components(n, edges))
