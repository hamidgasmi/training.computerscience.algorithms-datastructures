import sys
import random

def partitionSegments(starts, ends, l, r):
    p = random.randint(l, r)
    starts[p], starts[r] = starts[r], starts[p]
    ends[p], ends[r] = ends[r], ends[p]

    p = l - 1
    for j in range(l, r):
        if starts[j] < starts[r] or (starts[j] == starts[r] and ends[j] <= ends[r]):
            p += 1
            starts[p], starts[j] = starts[j], starts[p]
            ends[p], ends[j] = ends[j], ends[p]
    
    starts[p + 1], starts[r] = starts[r], starts[p + 1]
    ends[p + 1], ends[r] = ends[r], ends[p + 1]

    return p + 1

def quickSortSegments(starts, ends, l, r):
    
    while l < r:
        p = partitionSegments(starts, ends, l, r)
        if (p - l) < r - p:
            quickSortSegments(starts, ends, l, p - 1)
            l = p + 1
        else:
            quickSortSegments(starts, ends, p + 1, r)
            r = p - 1

def partitionPoints(points, initPos, l, r):
    p = random.randint(l, r)
    points[p], points[r] = points[r], points[p]
    initPos[p], initPos[r] = initPos[r], initPos[p]

    p = l - 1
    for j in range(l, r):
        if points[j] <= points[r]:
            p += 1
            points[p], points[j] = points[j], points[p]
            initPos[p], initPos[j] = initPos[j], initPos[p]

    p += 1
    points[p], points[r] = points[r], points[p]
    initPos[p], initPos[r] = initPos[r], initPos[p]

    return p

def quickSortPoints(points, initPos, l, r):
    while l < r:
        p =  partitionPoints(points, initPos, l, r)
        if p - l < r - p:
            quickSortPoints(points, initPos, l, p - 1)
            l = p + 1
        else:
            quickSortPoints(points, initPos, p + 1, r)
            r = p - 1

def fast_count_segments(starts, ends, points):
    

    quickSortSegments(starts, ends, 0, len(ends) - 1)
    
    initPos = len(points) * [0]
    for p in range(len(points)): 
        initPos[p] = p
    quickSortPoints(points, initPos, 0, len(points) - 1)
    
    s = 0
    e = 0 
    p = 0
    segmentCnt = 0
    cnt = [0] * len(points)
    point = 0
    while (s < len(starts) or e < len(ends)) and p < len(points):
        if s < len(starts):
            point = min(starts[s], ends[e], points[p])
        else:
            point = min(ends[e], points[p])

        if s < len(starts) and point == starts[s]:
            segmentCnt += 1
            s += 1
        
        if  point == points[p]:
            cnt[initPos[p]] = segmentCnt
            p += 1

        if e < len(ends) and point == ends[e]:
            segmentCnt -= 1
            e += 1

    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    cnt = fast_count_segments(starts, ends, points)

    for x in cnt:
        print(x, end=' ')

#python3 points_and_segments.py <<< "2 3 0 5 7 10 1 6 11" 1 0 0
#python3 points_and_segments.py <<< "1 3 -10 10 -100 100 0" 0 0 1
#python3 points_and_segments.py <<< "3 2 0 5 -3 2 7 10 1 6" 2 0
