import sys
import math
import random
from closest_v1 import minimum_distance_naive

def merge(x, y, left, mid, right):
    l = left
    r = mid + 1
    xs = []
    ys = []
    while l <= mid and r <= right: 
        if x[l] <= x[r]:
            xs.append(x[l])
            ys.append(y[l])
            l += 1
        else:
            xs.append(x[r])
            ys.append(y[r])
            r += 1

    while l <= mid:
        xs.append(x[l])
        ys.append(y[l])
        l += 1
    
    while r <= right:
        xs.append(x[r])
        ys.append(y[r])
        r += 1

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
    
def minDistance(xx, yx, xy, yy, l, r):
    if l == r:
        return 10 ** 10
    elif l + 1 == r:
        return math.sqrt((xx[l] - xx[r]) ** 2 + (yx[l] - yx[r]) ** 2)

    m = (l + r) // 2
    d = minDistance(xx, yx, xy, yy, l, m)
    d = min(d, minDistance(xx, yx, xy, yy, m + 1, r))
    if d <= 0.0000000001: return d

    stripx = []
    stripy = []
    for i in range(l, r + 1):
        if abs(xy[i] - xx[m]) < d:
            stripx.append(xy[i])
            stripy.append(yy[i])

    for i in range(len(stripx)):
        for j in range(i + 1, min(len(stripx), i + 8)):
            d = min(d, math.sqrt((stripx[i] - stripx[j]) ** 2 + (stripy[i] - stripy[j]) ** 2))

    return d

def minimum_distance(x, y):

    xy = [0] * len(x)
    yy = [0] * len(y)
    for i in range(len(x)):
        xy[i] = x[i]
        yy[i] = y[i]

    mergeSort(x, y, 0, len(y) - 1)
    mergeSort(yy, xy, 0, len(xy) - 1)

    return minDistance(x, y, xy, yy, 0, len(x) - 1)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance_naive(x, y, 0, len(x) - 1)))
    print("{0:.9f}".format(minimum_distance(x, y)))
    assert(minimum_distance([3], [3]) == minimum_distance_naive([3], [3], 0, 0))
    assert(minimum_distance([-1000000000, -1000000000], [1000000000, 1000000000]) == minimum_distance_naive([-1000000000, -1000000000], [1000000000, 1000000000], 0, 1))
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
#python3 closest_v3.py <<< "4 1 150 1 100 50 100 50 150"


#Failed case #13/23: time limit exceeded (Time used: 20.05/10.00, memory used: 13570048/536870912.)
#Failed case #12/23: Wrong answer (Time used: 1.10/10.00, memory used: 11624448/536870912.)