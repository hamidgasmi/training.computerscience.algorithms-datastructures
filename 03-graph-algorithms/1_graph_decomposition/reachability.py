import sys
from queue import Queue 

class MazeGraph:
    def __init__(self, n, edges):
        self.adj = [[] for _ in range(n)]
        self.buildAdjacencyList(edges)
        self.visited = [False] * n

    # Time Complexity: O(|E|)
    # Space Complexity: O(1)
    def buildAdjacencyList(self, edges):
        for (a, b) in edges:
            self.adj[a - 1].append(b - 1)
            self.adj[b - 1].append(a - 1)

    def visit(self, v):
        self.visited[v] = True

    def isVisited(self, v):
        return self.visited[v]

    def explore(self, u, v, solution):
        if solution == 1:
            return self.explore_dfs(u, v)
        elif solution == 2:
            self.enqueued = [False] * n
            q = Queue(maxsize = len(self.visited))
            return self.explore_bfs(u, v, q)
        else:
            return 0

    # Time Complexity: O(|V| + |E|):
    # .... Each vertex is explored exactly once
    # .... Each vertex checks each neighbor
    # Space Complexity: O(|V|):
    # .... Each vertex calls recursively explore method for 1 neighbor at a time
    # Result: Good job! (Max time used: 0.03/5.00, max memory used: 9535488/536870912.)
    def explore_dfs(self, u, v):
        if u == v:
            return 1

        self.visit(u)
        for a in self.adj[u]:
            if not self.isVisited(a):
                if self.explore_dfs(a, v) == 1:
                    return 1

        return 0

    # Time Complexity: O(|V| + |E|)
    # .... Each vertex is explored exactly once
    # .... Each vertex checks each neighbor
    # Space Complexity: O(|V|):
    # .... Each vertex is enqueued only once
    # Result: Good job! (Max time used: 0.05/5.00, max memory used: 10067968/536870912.) 
    def explore_bfs(self, u, v, q):
        if u == v:
            return 1

        q.put(u)
        while not q.empty():
            u = q.get()
            if u == v:
                return 1
            self.visit(u)

            for a in self.adj[u]:
                self.enqueue(q, a)
        return 0

    def enqueue(self, q, v):
        if not self.enqueued[v]:
            q.put(v)
            self.enqueued[v] = True

def reach(n, edges, u, v, solution):

    if 1 <= solution <= 2:
        aMaze = MazeGraph(n, edges)
        return aMaze.explore(u, v, solution)

    elif 3 <= solution == 4:
        return 0
        # see reachability-disjoint-sets.py
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    x, y = x - 1, y - 1

    print(reach(n, edges, x, y, 1))
