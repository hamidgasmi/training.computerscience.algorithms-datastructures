import sys
import random

def partition(points, l, r):
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

def quickSort(points, l, r):
    while l < r:
        p =  partition(points, l, r)
        if p - l < r - p:
            quickSort(points, l, p - 1)
            l = p + 1
        else:
            quickSort(points, p + 1, r)
            r = p - 1

def binarySearch(points, p, l, r):
    if l > r:
        return l - 1
    elif points[l] == p and points[l + 1] == p:
        return binarySearch(points, p, l + 1, r)

    mid = (r + l) // 2
    if points[mid] == p:
        return mid
    elif points[mid] > p:
        return binarySearch(points, p, l, mid - 1)
    else:
        return binarySearch(points, p, mid + 1, r)

def fast_count_segments(starts, ends, points):
    quickSort(starts, 0, len(starts) - 1)
    quickSort(ends, 0, len(ends) - 1)

    print("Starts", starts)
    print("Ends", ends)
    cnt = [0] * len(points)
    for p in range(len(points)):
        s = binarySearch(starts, points[p], 0, len(starts) - 1)
        e = binarySearch(ends, points[p], 0, len(ends) - 1)
        cnt[p] = s - e

        print("P: ", points[p])
        print("S: ", s)
        print("E: ", e)

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

#python3 points_and_segments_v4.py <<< "3 4 0 0 0 5 7 10 0 1 6 11" 2 1 0 0
#python3 points_and_segments_v4.py <<< "6 4 0 0 0 5 7 10 12 12 20 25 17 26 0 1 6 11" 2 1 0 0
#python3 points_and_segments_v4.py <<< "7 4 0 0 0 5 7 10 12 12 20 25 17 26 19 29 0 1 6 11" 2 1 0 0
#python3 points_and_segments_v4.py <<< "2 3 0 5 7 10 1 6 11" 1 0 0
#python3 points_and_segments_v4.py <<< "1 3 -10 10 -100 100 0" 0 0 1
#python3 points_and_segments_v4.py <<< "3 2 0 5 -3 2 7 10 1 6" 2 0
