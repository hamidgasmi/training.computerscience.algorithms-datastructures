import sys
import math

def merge(x, y, left, mid, right):
    l = left
    r = mid + 1
    xs = [0 for i in range(right - left + 1)]
    ys = [0 for i in range(right - left + 1)]
    i = 0
    while l <= mid and r <= right: 
        if x[l] <= x[r]:
            xs[i] = x[l]
            ys[i] = y[l]
            l += 1
        else:
            xs[i] = x[r]
            ys[i] = y[r]
            r += 1
        i += 1

    while l <= mid:
        xs[i] = x[l]
        ys[i] = y[l]
        l += 1
        i += 1
    
    while r <= right:
        xs[i] = x[r]
        ys[i] = y[r]
        r += 1
        i += 1

    for i in range(left, right + 1):
        x[i] = xs[i - left]
        y[i] = ys[i - left]

def mergeSort(x, y, l, r):
    if l >= r:
        return

    m = (r + l) // 2
    mergeSort(x, y, l, m)
    mergeSort(x, y, m + 1, r)

    merge(x, y, l, m, r)

def distance(xi, yi, xj, yj):
    return math.sqrt(pow(xi - xj, 2) + pow(yi - yj, 2))

def minDistance(xx, yx, xy, yy, l, r):
    if l >= r: 
        return 2830000000  #The max value of d is 2 * sqrt(2) * 10^9
    elif l + 1 == r:
        return distance(xx[l], yx[l], xx[r], yx[r])
    elif l + 3 == r:
        return minimum_distance_naive(xx, yx, l, r)

    m = (l + r) // 2
    leftxy = []
    leftyy = []
    rightxy = []
    rightyy = []
    for i in range(len(xy)):
        if xy[i] <= xx[m]: #and len(leftxy) < m - l + 1
            leftxy.append(xy[i])
            leftyy.append(yy[i])
        else:
            rightxy.append(xy[i])
            rightyy.append(yy[i])

    dl = minDistance(xx, yx, leftxy, leftyy, l, m)
    dr = minDistance(xx, yx, rightxy, rightyy, m + 1, r)
    d = min(dl, dr)

    stripx = []
    stripy = []
    for i in range(len(xy)):
        if abs(xy[i] - xx[m]) < d:
            stripx.append(xy[i])
            stripy.append(yy[i])

    for i in range(len(stripx)):
        j = i + 1
        while j < len(stripx) and stripy[j] - stripy[i] < d:
            d = min(d, distance(stripx[i], stripy[i], stripx[j], stripy[j]))
            j += 1

    return d

def minimum_distance_naive(x, y, l, r):
    d = 2830000000 #The max value of d is 2 * sqrt(2) * 10^9
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            d = min(d, distance(x[i], y[i], x[j], y[j]))

    return d

def minimum_distance(xx, yx):

    xy = [xx[i] for i in range(len(xx))]
    yy = [yx[i] for i in range(len(xx))]

    mergeSort(xx, yx, 0, len(xx) - 1)
    mergeSort(yy, xy, 0, len(xy) - 1)

    return minDistance(xx, yx, xy, yy, 0, len(xx) - 1)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]

    print("{0:.9f}".format(minimum_distance_naive(x, y, 0, len(x) - 1)))
    print("{0:.9f}".format(minimum_distance(x, y)))
    assert(minimum_distance([3], [3]) == minimum_distance_naive([3], [3], 0, 0))
    assert(minimum_distance([pow(10, 9), pow(-10, 9)], [pow(10, 9), pow(-10, 9)]) == minimum_distance_naive([pow(10, 9), pow(-10, 9)], [pow(10, 9), pow(-10, 9)], 0, 1))
    assert(minimum_distance([0, 3], [0, 4]) == minimum_distance_naive([0, 3], [0, 4], 0, 1))
    assert(minimum_distance([1, 2, 100], [100, 50, 100]) == minimum_distance_naive([1, 2, 100], [100, 50, 100], 0, 2))
    assert(minimum_distance([3, 0, 0, 0], [3, 0, 0, 0]) == minimum_distance_naive([3, 0, 0, 0], [3, 0, 0, 0], 0, 3))
    assert(minimum_distance([3, 0, 0, 0], [3, 1, 2, 3]) == minimum_distance_naive([3, 0, 0, 0], [3, 1, 2, 3], 0, 3))
    assert(minimum_distance([3, 1, 2, 3], [3, 0, 0, 0]) == minimum_distance_naive([3, 1, 2, 3], [3, 0, 0, 0], 0, 3))
    assert(minimum_distance([4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2], [4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4]) == minimum_distance_naive([4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2], [4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4], 0, 10))
    assert(minimum_distance([4, -2, -3, -1, 2, -5, 1, -1, 3, -4, -2], [4, -2, -4, 3, -1, 0, 1, -1, -1, 2, 4]) == minimum_distance_naive([4, -2, -3, -1, 2, -5, 1, -1, 3, -4, -2], [4, -2, -4, 3, -1, 0, 1, -1, -1, 2, 4], 0, 10))
    assert(minimum_distance([-3, -14, -7, 26, 18, 38, 29, -48], [-8, -3, 5, 9, 99, 29, 72, 8]) == minimum_distance_naive([-3, -14, -7, 26, 18, 38, 29, -48], [-8, -3, 5, 9, 99, 29, 72, 8], 0, 7))
    assert(minimum_distance([2, 12, 40, 5, 12, 3], [3, 30, 50, 1, 10, 4]) == minimum_distance_naive([2, 12, 40, 5, 12, 3], [3, 30, 50, 1, 10, 4], 0, 5))

#python3 closest_v3.py <<< "2 0 0 3 4" 5.0
#python3 closest_v3.py <<< "4 7 7 1 100 4 8 7 7" 0.0 
#python3 closest_v3.py <<< "11 4 4 -2 -2 -3 -4 -1 3 2 3 -4 0 1 1 -1 -1 3 -1 -4 2 -2 4" 1.414213
#python3 closest_v3.py <<< "11 4 4 -2 -2 -3 -4 -1 3 2 -1 -5 0 1 1 -1 -1 3 -1 -4 2 -2 4" 1.414213
#python3 closest_v3.py <<< "12 4 4 -2 -2 -3 -4 -1 3 2 3 -4 0 1 1 -1 -1 3 -1 -4 2 -2 4 4 5"
#python3 closest_v3.py <<< "5 2 3 12 30 40 50 5 1 12 10 3 4"
#python3 closest_v3.py <<< "2 -1000000000 -1000000000 1000000000 1000000000"
#python3 closest_v3.py <<< "8 2 496 12 30 40 50 5 1 12 10 3 4 1 496 1 497"
#python3 closest_v3.py <<< "3 1 100 2 50 100 100"
#python3 closest_v3.py <<< "4 1 150 1 100 50 100 50 150" 49.0000