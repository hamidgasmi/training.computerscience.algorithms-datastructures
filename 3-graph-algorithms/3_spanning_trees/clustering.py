#Uses python3
import sys
import math
from collections import namedtuple
from operator import attrgetter

Edge = namedtuple('Edge', ['p1', 'p2', 'distance'])

class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1 for i in range(n)]

    def find(self, u):
        if self.parents[u] == u:
            return u

        r = self.find(self.parents[u])
        self.parents[u] = r

        return r

    def union(self, u, v):
        ru = self.find(u)
        rv = self.find(v)

        if ru == rv:
            return

        if self.ranks[ru] > self.ranks[rv]:
            self.parents[rv] = ru
        else:
            self.parents[ru] = rv
            if self.ranks[ru] == self.ranks[rv]:
                self.ranks[rv] += 1
    
def clustering(n, x, y, k):
    
    dijoint_set = DisjointSet(n)
    edges = []
    for i in range(n):
        for j in range(n):
            if i == j: 
                continue
            edges.append(Edge(i, j, math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)))
    edges.sort(key=lambda x:getattr(x, 'distance'))
    
    d = 3 * 10**6
    clusters_count = n
    for e in edges:

        if dijoint_set.find(e.p1) == dijoint_set.find(e.p2):
            continue

        if clusters_count == k and d > e.distance:
            d = e.distance
            continue

        dijoint_set.union(e.p1, e.p2)
        clusters_count -= 1

    return d

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(n, x, y, k)))
