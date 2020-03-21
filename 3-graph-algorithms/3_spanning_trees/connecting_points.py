#Uses python3
import sys
import math
import queue
from collections import namedtuple

Point  = namedtuple('Point', ['len', 'x', 'y', 'index'])

def minimum_distance(x, y):
    
    n = len(x)
    visited = [False] * n
    parents = [-1] * n

    infinity = 3 * 10**3
    distances = [infinity] * n
    distances[0] = 0

    hq = queue.PriorityQueue()
    for i in range(1, n):
        hq.put(Point(infinity, x[i], y[i], i))
    hq.put(Point(0, x[0], y[0], 0))

    while not hq.empty():
        p = hq.get()
        visited[p.index] = True
        #print("(i, x, y, distances): ", p.index, p.x, p.y, distances)
        #print("hq.empty", "empty" if hq.empty() else "not empty")
        for i in range(n):
            if not visited[i]:
                candidate_distance = math.sqrt((p.x - x[i])**2 + (p.y - y[i])**2)
                if distances[i] > candidate_distance:
                    distances[i] = candidate_distance
                    parents[i] = p.index
                    hq.put(Point(distances[i], x[i], y[i], i))

    result = 0.
    for d in distances:
        result += d

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
