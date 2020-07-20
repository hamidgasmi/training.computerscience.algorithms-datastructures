import sys

class Graph:
    def __init__(self, n, edges):
        
        self._vertices_count = n

        self._build_adjacency_list(edges)
    
    # Time Complexity: O(|E|)
    # Space Complexity: O(1)
    def _build_adjacency_list(self, edges):

        self._adjacency_list = [[] for _ in range(self._vertices_count)]
        for (a, b) in edges:
            self._adjacency_list[a - 1].append(b - 1)
    
    def explore(self, v, visited, cycle, order):

        visited[v] = True
        cycle[v] = True
        for a in self._adjacency_list[v]:
            if cycle[a]:
                return

            elif visited[a]:
                continue
            
            self.explore(a, visited, cycle, order)
            if cycle[a]:
                return
        
        order.append(v)
        cycle[v] = False

    def toposort_dfs(self):

        visited = [False for _ in range(self._vertices_count)]
        cycle = [False for _ in range(self._vertices_count)]

        order = []
        for v in range(self._vertices_count):
            if visited[v]:
                continue

            self.explore(v, visited, cycle, order)
            if cycle[v]:
                order.clear()
                break
        
        return order[::-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    
    graph = Graph(n, edges)
    order = graph.toposort_dfs()
    for x in order:
        print(x + 1, end=' ')

