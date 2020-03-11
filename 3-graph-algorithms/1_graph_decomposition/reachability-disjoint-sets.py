import sys
from abc import ABC, abstractmethod 

class DisjointSets(ABC):
    def __init__(self, n, edges):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.buildDisjointSets(edges)
    
    # Time Complexity: O(|E|)
    # Space Complexity: O(1)
    def buildDisjointSets(self, edges):
        for i in range(0, len(edges)):
            self.union(edges[i][0] - 1, edges[i][1] - 1)

    @abstractmethod
    def find(self, v):
        pass
    
    # Time Complexity: O(log |V|)
    # Space Complexity: O(1)
    def union(self, u, v):
        ru = self.find(u)
        rv = self.find(v)

        if ru == rv:
            return

        if self.rank[ru] >= self.rank[rv]:
            self.parent[rv] = ru

            if self.rank[ru] == self.rank[rv]:
                self.rank[ru] += 1
        else:
            self.parent[ru] = rv

class MazeDisjointSetRankHeuristic(DisjointSets):
    # Time Complexity: O(log |V|)
    # Space Complexity: O(1)
    def find(self, v):
        while self.parent[v] != v:
            v = self.parent[v]

        return v            
    
class MazeDisjointSetCompressPathHeuristic(DisjointSets):
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])

        return self.parent[v]

def reach(edges, n, u, v, solution):

    if solution == 3:
        # Good job! (Max time used: 0.04/5.00, max memory used: 10145792/536870912.)
        aMazeSets = MazeDisjointSetRankHeuristic(n, edges)
        return 1 if aMazeSets.find(u) == aMazeSets.find(v) else 0

    elif solution == 4:
        # Good job! (Time used: 0.04/5.00, memory used: 9732096/536870912.)
        aMazeSets = MazeDisjointSetCompressPathHeuristic(n, edges)
        return 1 if aMazeSets.find(u) == aMazeSets.find(v) else 0

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
    
    print(reach(edges, n, x, y, 3))
