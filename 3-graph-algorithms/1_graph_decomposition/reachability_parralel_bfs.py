import sys
from queue import Queue
import threading

class MazeGraph:
    
    result = 0
    s = set()
    lock = threading.Lock()

    def __init__(self, n, adj):
        self.adj = adj
        self.visited = [False] * n
        self.enqueued = [False] * n
        self.q = Queue(n)

    def visit(self, v):
        self.visited[v] = True

        if v in MazeGraph.s:
            MazeGraph.lock.acquire()
            MazeGraph.result = 1
            endThread = True
            MazeGraph.lock.release()
        else:
            MazeGraph.lock.acquire()
            MazeGraph.s.add(v)
            MazeGraph.lock.release()
            endThread = MazeGraph.result == 1

        return endThread

    def isVisited(self, v, visited):
        return visited[v]

    def enqueue(self, v):
        if not self.enqueued[v]:
            self.q.put(v)
            self.enqueued[v] = True

    # Time Complexity: O(|V| + |E|)
    # Space Complexity: O(|V|):
    def explore(self, u):
        self.enqueue(u)
        while not self.q.empty():
            u = self.q.get()
            if self.visit(u):
                return 1

            for i in range(len(self.adj[u])):
                self.enqueue(self.adj[u][i])

        return 0

def reach(n, edges, u, v):
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    aMaze1 = MazeGraph(n, adj)
    aMaze2 = MazeGraph(n, adj)

    t1 = threading.Thread(target=aMaze1.explore, args=(u, ))
    t2 = threading.Thread(target=aMaze2.explore, args=(v, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return MazeGraph.result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    x, y = x - 1, y - 1

    print(reach(n, edges, x, y))
