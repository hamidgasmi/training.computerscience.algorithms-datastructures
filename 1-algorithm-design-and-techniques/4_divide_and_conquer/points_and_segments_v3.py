import sys
import random

def comparePoint(p1, p2, attr1, attr2):
    if p1 < p2:
        return True
    elif p1 > p2:
        return False
    elif p1 == p2 and attr1 == attr2:
        return True
    elif p1 == p2 and attr1 == -1:
        return True
    elif p1 == p2 and attr1 >= 0 and attr2 == -2:
        return True
    else:
        return False

def partitionPoints(points, IniAttr, l, r):
    p = random.randint(l, r)
    points[p], points[r] = points[r], points[p]
    IniAttr[p], IniAttr[r] = IniAttr[r], IniAttr[p]

    p = l - 1
    for j in range(l, r):
        if comparePoint(points[j], points[r], IniAttr[j], IniAttr[r]):
            p += 1
            points[p], points[j] = points[j], points[p]
            IniAttr[p], IniAttr[j] = IniAttr[j], IniAttr[p]

    p += 1
    points[p], points[r] = points[r], points[p]
    IniAttr[p], IniAttr[r] = IniAttr[r], IniAttr[p]

    return p

# Points are sorted by location and type: for the same location, start points should come 1st, points should come 2nd and after ends should come 3rd
# Time complexity: O([s + p] log[s + p])
def quickSortPoints(points, IniAttr, l, r):
    while l < r:
        p =  partitionPoints(points, IniAttr, l, r)
        if p - l < r - p:
            quickSortPoints(points, IniAttr, l, p - 1)
            l = p + 1
        else:
            quickSortPoints(points, IniAttr, p + 1, r)
            r = p - 1

def fast_count_segments(starts, ends, points):
    
    # Merge all points in the same lists: start points, end points, points
    allPoints = []
    allPoints.extend(starts)
    pointAttr = [-1 for i in range(len(starts))]
    allPoints.extend(points)
    pointAttr.extend([i for i in range(len(points))])
    allPoints.extend(ends)
    pointAttr.extend([-2 for i in range(len(ends))])
    
    #Sort all point
    quickSortPoints(allPoints, pointAttr, 0, len(allPoints) - 1)

    cnt = [0] * len(points)
    p = 0
    segmentCnt = 0
    pntCnt = 0
    while p < len(allPoints):
        if pointAttr[p] == -1:
            segmentCnt += 1
        elif pointAttr[p] >= 0:
            cnt[pointAttr[p]] += segmentCnt
            pntCnt += 1
            if pntCnt == len(points): break
        elif pointAttr[p] == -2:
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

#python3 points_and_segments_v3.py <<< "3 4 0 0 0 5 7 10 0 1 6 11" 2 1 0 0
#python3 points_and_segments_v3.py <<< "6 4 0 0 0 5 7 10 12 12 20 25 17 26 0 1 6 11" 2 1 0 0
#python3 points_and_segments_v3.py <<< "2 3 0 5 7 10 1 6 11" 1 0 0
#python3 points_and_segments_v3.py <<< "1 3 -10 10 -100 100 0" 0 0 1
#python3 points_and_segments_v3.py <<< "3 2 0 5 -3 2 7 10 1 6" 2 0