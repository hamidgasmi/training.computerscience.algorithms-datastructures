import sys
import random

def partitionPoints1(points, l, r):
    p = random.randint(l, r)
    points[p], points[r] = points[r], points[p]

    p = l - 1
    for j in range(l, r):
        if points[j] <= points[r]:
            p += 1
            points[p], points[j] = points[j], points[p]

    p += 1
    points[p], points[r] = points[r], points[p]

    return p

def quickSortPoints1(points, l, r):
    while l < r:
        p =  partitionPoints1(points, l, r)
        if p - l < r - p:
            quickSortPoints1(points, l, p - 1)
            l = p + 1
        else:
            quickSortPoints1(points, p + 1, r)
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

def mergePoints(starts, ends, points, allPoints, allPointsTypes):
    s = 0
    e = 0
    p = 0

    p = 0
    for i in range(len(starts)):
        allPoints[p] = starts[i]
        allPointsTypes[p] = 1
        p += 1
    


        allPoints[p] = ends[i]
        allPointsTypes[p] = 3
    
    for i in range(len(allPoints)):
        if s < len(starts)


def fast_count_segments(starts, ends, points):
    
    quickSortPoints1(ends, 0, len(ends) - 1)
    quickSortPoints1(starts, 0, len(ends) - 1)
    
    initPos = len(points) * [0]
    for p in range(len(points)): 
        initPos[p] = p
    quickSortPoints(points, initPos, 0, len(points) - 1)

    allPoints = 0 * [2 * len(ends) + len(points)]
    pointTypes = '' * [2 * len(ends) + len(points)]
    mergePoints(starts, ends, points, allPoints, pointTypes)
    cnt = [0] * len(points)
    p = 0
    i = 0
    segmentCnt = 0
    while p < len(allPoints):
        if pointTypes[p] == 1:
            segmentCnt += 1
        elif pointTypes[p] == 2:
            cnt[initPos[i]] += segmentCnt
            i += 1
        elif pointTypes[p] == 3:
            segmentCnt -= 1
        p += 1

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

#python3 points_and_segments_enhanced.py <<< "2 3 0 5 7 10 1 6 11" 1 0 0
#python3 points_and_segments_enhanced.py <<< "1 3 -10 10 -100 100 0" 0 0 1
#python3 points_and_segments_enhanced.py <<< "3 2 0 5 -3 2 7 10 1 6" 2 0
