import sys
from queue import Queue 

class MazeGraph:
    def __init__(self, n, adj, solution):
        self.adj = adj
        self.visited = [False] * n
        if solution == 2:
            self.enqueued = [False] * n

    def visit(self, v):
        self.visited[v] = True

    def enqueue(self, q, v):
        if not self.enqueued[v]:
            q.put(v)
            self.enqueued[v] = True

    def isVisited(self, v):
        return self.visited[v]

    # Time Complexity: O(|V| + |E|):
    # .... Each vertex is explored exactly once
    # .... Each vertex checks each neighbor
    # Space Complexity: O(|V|):
    # .... Each vertex calls explore method recursively for 1 neighbor at a time
    # Good job! (Max time used: 0.03/5.00, max memory used: 9535488/536870912.)
    def explore_dfs(self, u, v):
        if u == v:
            return 1

        self.visit(u)
        for i in range(len(adj[u])):
            if not self.isVisited(adj[u][i]):
                if self.explore_dfs(adj[u][i], v) == 1:
                    return 1

        return 0

    # Time Complexity: O(|V| + |E|)
    # .... Each vertex is explored exactly once
    # .... Each vertex checks each neighbor
    # Space Complexity: O(|V|):
    # .... Each vertex is enqueued only once
    # Result: Good job! (Max time used: 0.04/5.00, max memory used: 10084352/536870912.)
    def explore_bfs(self, u, v, q):
        if u == v:
            return 1

        q.put(u)
        while not q.empty():
            u = q.get()
            if u == v:
                return 1
            self.visit(u)

            for i in range(len(adj[u])):
                self.enqueue(q, adj[u][i])
               
        return 0

def reach(adj, n, u, v, solution):

    aMaze = MazeGraph(n, adj, solution)
    if solution == 1:
        return aMaze.explore_dfs(u, v) 
    elif solution == 2:
        q = Queue(maxsize = n) 
        return aMaze.explore_bfs(u, v, q)
    elif solution == 3:
        return 0
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    print(reach(adj, n, x, y, 2))
