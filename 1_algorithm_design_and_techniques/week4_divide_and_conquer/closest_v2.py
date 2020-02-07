import sys
import math
import random

def partition(x, y, l, r):
    p = random.randint(l, r)
    x[p], x[r] = x[r], x[p]
    y[p], y[r] = y[r], y[p]

    p = l - 1
    for j in range(l, r):
        if x[j] <= x[r]:
            p += 1
            x[p], x[j] = x[j], x[p]
            y[p], y[j] = y[j], y[p]
    p += 1
    x[p], x[r] = x[r], x[p]
    y[p], y[r] = y[r], y[p]

    return p

def quickSort(x, y, l, r):
    while l < r:
        p =  partition(x, y, l, r)
        if p - l < r - p:
            quickSort(x, y, l, p - 1)
            l = p + 1
        else:
            quickSort(x, y, p + 1, r)
            r = p - 1

def distance(xi, yi, xj, yj):
    return math.sqrt(pow(xi - xj, 2) + pow(yi - yj, 2))

def minDistance(xx, yx, xy, yy, l, r):
    if l == r:
        return 10 ** 10
    if l + 1 == r:
        return distance(xx[l], yx[l], xx[r], yx[r])
    elif l + 3 == r:
        return minimum_distance_naive(xx, yx, l, r)

    m = (l + r) // 2

    leftxy = []
    leftyy = []
    rightxy = []
    rightyy = []
    for i in range(len(xy)):
        if xy[i] <= xx[m] and len(leftxy) < m - l + 1:
            leftxy.append(xy[i])
            leftyy.append(yy[i])
        else:
            rightxy.append(xy[i])
            rightyy.append(yy[i])

    d = minDistance(xx, yx, leftxy, leftyy, l, m)
    d = min(d, minDistance(xx, yx, rightxy, rightyy, m + 1, r))

    stripx = []
    stripy = []
    for i in range(len(xy)):
        if abs(xy[i] - xx[m]) < d:
            stripx.append(xy[i])
            stripy.append(yy[i])

    for i in range(len(stripx)):
        for j in range(i + 1, min(len(stripx), i + 7)):
            d = min(d, math.sqrt(pow(stripx[i] - stripx[j], 2) + pow(stripy[i] - stripy[j], 2)))

    return d

def minimum_distance_naive(x, y, l, r):
    d = 10 ** 10
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            d = min(d, distance(x[i], y[i], x[j], y[j]))

    return d

def minimum_distance(x, y):

    xy = [0] * len(x)
    yy = [0] * len(y)
    for i in range(len(x)):
        xy[i] = x[i]
        yy[i] = y[i]

    quickSort(x, y, 0, len(y) - 1)
    quickSort(yy, xy, 0, len(xy) - 1)

    return minDistance(x, y, xy, yy, 0, len(x) - 1)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
    print("{0:.9f}".format(minimum_distance_naive(x, y, 0, len(x) - 1)))
    assert(minimum_distance([3], [3]) == minimum_distance_naive([3], [3], 0, 0))
    assert(minimum_distance([-1000000000, -1000000000], [1000000000, 1000000000]) == minimum_distance_naive([-1000000000, -1000000000], [1000000000, 1000000000], 0, 1))
    assert(minimum_distance([0, 3], [0, 4]) == minimum_distance_naive([0, 3], [0, 4], 0, 1))
    assert(minimum_distance([3, 0, 0, 0], [3, 0, 0, 0]) == minimum_distance_naive([3, 0, 0, 0], [3, 0, 0, 0], 0, 3))
    assert(minimum_distance([3, 0, 0, 0], [3, 1, 2, 3]) == minimum_distance_naive([3, 0, 0, 0], [3, 1, 2, 3], 0, 3))
    assert(minimum_distance([3, 1, 2, 3], [3, 0, 0, 0]) == minimum_distance_naive([3, 1, 2, 3], [3, 0, 0, 0], 0, 3))
    assert(minimum_distance([4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2], [4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4]) == minimum_distance_naive([4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2], [4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4], 0, 10))
    assert(minimum_distance([4, -2, -3, -1, 2, -5, 1, -1, 3, -4, -2], [4, -2, -4, 3, -1, 0, 1, -1, -1, 2, 4]) == minimum_distance_naive([4, -2, -3, -1, 2, -5, 1, -1, 3, -4, -2], [4, -2, -4, 3, -1, 0, 1, -1, -1, 2, 4], 0, 10))
    assert(minimum_distance([-3, -14, -7, 26, 18, 38, 29, -48], [-8, -3, 5, 9, 99, 29, 72, 8]) == minimum_distance_naive([-3, -14, -7, 26, 18, 38, 29, -48], [-8, -3, 5, 9, 99, 29, 72, 8], 0, 7))
    assert(minimum_distance([2, 12, 40, 5, 12, 3], [3, 30, 50, 1, 10, 4]) == minimum_distance_naive([2, 12, 40, 5, 12, 3], [3, 30, 50, 1, 10, 4], 0, 5))

#python3 closest_v2.py <<< "2 0 0 3 4" 5.0
#python3 closest_v2.py <<< "4 7 7 1 100 4 8 7 7" 0.0 
#python3 closest_v2.py <<< "11 4 4 -2 -2 -3 -4 -1 3 2 3 -4 0 1 1 -1 -1 3 -1 -4 2 -2 4" 1.414213
#python3 closest_v2.py <<< "11 4 4 -2 -2 -3 -4 -1 3 2 -1 -5 0 1 1 -1 -1 3 -1 -4 2 -2 4" 1.414213
#python3 closest_v2.py <<< "12 4 4 -2 -2 -3 -4 -1 3 2 3 -4 0 1 1 -1 -1 3 -1 -4 2 -2 4 4 5"
#python3 closest_v2.py <<< "5 2 3 12 30 40 50 5 1 12 10 3 4"
#python3 closest_v2.py <<< "2 -1000000000 -1000000000 1000000000 1000000000"
#python3 closest_v2.py <<< "8 2 496 12 30 40 50 5 1 12 10 3 4 1 496 1 497"
#Failed case #13/23: time limit exceeded (Time used: 20.05/10.00, memory used: 13570048/536870912.)
#Failed case #21/23: time limit exceeded (Time used: 599.86/10.00, memory used: 33521664/536870912.)
