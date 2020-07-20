import sys

class Graph:
    def __init__(self, n, edges):
        
        self._vertices_count = n

        self._build_adjacency_list(edges)
    
    # Time Complexity: O(|E|)
    # Space Complexity: O(|V|)
    def _build_adjacency_list(self, edges):

        self._adjacency_list = [[] for _ in range(self._vertices_count)]
        self.indegree = [0 for _ in range(self._vertices_count)]
        for (a, b) in edges:
            self._adjacency_list[a - 1].append(b - 1)
            self.indegree[b - 1] += 1

    # Time Complexity: O(|V| + |E|)
    # Space Complexity: O(|V|)
    def toposort_indegree(self):

        # 1. Indgree array:
        indegree = self.indegree.copy()

        # 2. Zero indegree nodes:
        zero_indegree = []
        for v in range(self._vertices_count):
            if not indegree[v]:
                zero_indegree.append(v)

        # 3. Topological Sort
        i = 0
        topological_order = []
        while i < len(zero_indegree):
            v = zero_indegree[i]
            topological_order.append(v)

            for a in self._adjacency_list[v]:
               indegree[a] -= 1
               if not indegree[a]:
                   zero_indegree.append(a)

            i += 1
        
        return topological_order if len(topological_order) == self._vertices_count else []

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    
    graph = Graph(n, edges)
    order = graph.toposort_indegree()
    for x in order:
        print(x + 1, end=' ')

