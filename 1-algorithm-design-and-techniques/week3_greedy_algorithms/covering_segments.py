import sys
import random
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def swap(segments, i, j):
    if i < 0 or i >= len(segments): return
    if j < 0 or j >= len(segments): return

    aSegment = segments[i]
    segments[i] = segments[j]
    segments[j] = aSegment

def getRandomizedPartition(segments, p, r):
    if r < p: return
    if r > len(segments): return

    swap(segments, random.randrange (p, r + 1, 1), r)
    
    i = p - 1
    for j in range(p, r):
        if (segments[j].end <= segments[r].end):
            i += 1
            swap(segments, i, j)
    swap(segments, i + 1, r)

    return i + 1

def quickSortBySegmentEnd(segments, p, r):
    if p >= r: return

    q = getRandomizedPartition(segments, p, r)
    quickSortBySegmentEnd(segments, p, q - 1)
    quickSortBySegmentEnd(segments, q + 1, r)

# Time Complexity: O(n log n)
# 2. Greedy Algorithm:
# 2.1. Make a greedy choice: choose a segment i which end (Bi) is the min
# 2.2. Prove this choice is safe (Proof by contradiction):
# ..... Let's choose any point Ai < Bj < Bi => All segments that start between ]Bj, Bi] aren't included => we'll have at least 1 additional point
# ..... Let's choose any point Bj > Bi => All segments that end between [Bi, Bj[ aren't included => we'll have at least 1 additional point
# 2.3. Reduce to a subproblem: remove all segments that include Bi
# 2.4. Solve the subproblem (Iterate): Go to 2.1
def optimal_points(segments):

    quickSortBySegmentEnd(segments, 0, len(segments) - 1) #O(n log n)

    #Greedy Algorithm: O(n)
    points = []
    end = -1
    for s in segments:
        if s.start > end and s.end > end:
            points.append(s.end)
            end = s.end

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    #quickSortBySegmentEnd(segments, 0, len(segments) - 1)
    #print(segments)
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
#python3 covering_segments.py <<< "4 4 7 1 3 2 5 5 6"
#python3 covering_segments.py <<< "3 1 3 2 5 3 6"
#python3 covering_segments.py <<< "1 1 3"
#python3 covering_segments.py <<< "0"
#python3 covering_segments.py <<< "2 0 0 0 5"
#python3 covering_segments.py <<< "2 0 1 2 5"
#python3 covering_segments.py <<< "100 41 42 52 52 63 63 80 82 78 79 35 35 22 23 31 32 44 45 81 82 36 38 10 12 1 1 23 23 32 33 87 88 55 56 69 71 89 91 93 93 38 40 33 34 14 16 57 59 70 72 36 36 29 29 73 74 66 68 36 38 1 3 49 50 68 70 26 28 30 30 1 2 64 65 57 58 58 58 51 53 41 41 17 18 45 46 4 4 0 1 65 67 92 93 84 85 75 77 39 41 15 15 29 31 83 84 12 14 91 93 83 84 81 81 3 4 66 67 8 8 17 19 86 87 44 44 34 34 74 74 94 95 79 81 29 29 60 61 58 59 62 62 54 56 58 58 79 79 89 91 40 42 2 4 12 14 5 5 28 28 35 36 7 8 82 84 49 51 2 4 57 59 25 27 52 53 48 49 9 9 10 10 78 78 26 26 83 84 22 24 86 87 52 54 49 51 63 64 54 54"
