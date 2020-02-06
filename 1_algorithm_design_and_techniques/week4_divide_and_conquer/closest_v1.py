import sys
import math
import random

def compare(xi, yi, xj, yj):
    if xi < xj:
        return True
    elif xi > xj:
        return False
    elif xi == xj and yi <= yj:
        return True
    else:
        return False

def partition(x, y, l, r):
    p = random.randint(l, r)
    x[p], x[r] = x[r], x[p]
    y[p], y[r] = y[r], y[p]

    p = l - 1
    for j in range(l, r):
        if compare(x[j], y[j], x[r], y[r]):
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

def minDistance(x, y, l, r):
    if l == r:
        return 10 ** 10
    elif l + 1 == r:
        return (x[l] - x[r]) ** 2 + (y[l] - y[r]) ** 2

    m = (l + r) // 2
    d = minDistance(x, y, l, m)
    d = min(d, minDistance(x, y, m + 1, r))

    i = m
    while i - 1 >= 0 and (x[i - 1] - x[m]) ** 2 + (y[i - 1] - y[m]) ** 2 <= d:
        i -= 1
    j = m
    while j + 1 <= r and (x[j + 1] - x[m]) ** 2 + (y[j + 1] - y[m]) ** 2 <= d:
        j += 1

    xp = [x[k] for k in range(i, j + 1)]
    yp = [y[k] for k in range(i, j + 1)]
    quickSort(yp, xp, 0, j - i)
    for k in range(j - i + 1):
        for l in range(k + 1, min(j - i + 1, k + 8)):
            d = min(d, (xp[k] - xp[l]) ** 2 + (yp[k] - yp[l]) ** 2)

    return d

def minimum_distance(x, y):
    quickSort(x, y, 0, len(y) - 1)

    return math.sqrt(minDistance(x, y, 0, len(x) - 1))

def minimum_distance_naive(x, y):
    d = 10 ** 100
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            d = min(d, (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)

    return math.sqrt(d)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
    print("{0:.9f}".format(minimum_distance_naive(x, y)))
    assert(minimum_distance([3, 0, 0, 0], [3, 0, 0, 0]) == minimum_distance_naive([3, 0, 0, 0], [3, 0, 0, 0]))
    assert(minimum_distance([3, 0, 0, 0], [3, 1, 2, 3]) == minimum_distance_naive([3, 0, 0, 0], [3, 1, 2, 3]))
    assert(minimum_distance([3, 1, 2, 3], [3, 0, 0, 0]) == minimum_distance_naive([3, 1, 2, 3], [3, 0, 0, 0]))
    assert(minimum_distance([4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2], [4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4]) == minimum_distance_naive([4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2], [4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4]))
    assert(minimum_distance([4, -2, -3, -1, 2, -5, 1, -1, 3, -4, -2], [4, -2, -4, 3, -1, 0, 1, -1, -1, 2, 4]) == minimum_distance_naive([4, -2, -3, -1, 2, -5, 1, -1, 3, -4, -2], [4, -2, -4, 3, -1, 0, 1, -1, -1, 2, 4]))
    assert(minimum_distance([-1000000000, -1000000000], [1000000000, 1000000000]) == minimum_distance_naive([-1000000000, -1000000000], [1000000000, 1000000000]))
    assert(minimum_distance([-3, -14, -7, 26, 18, 38, 29, -48], [-8, -3, 5, 9, 99, 29, 72, 8]) == minimum_distance_naive([-3, -14, -7, 26, 18, 38, 29, -48], [-8, -3, 5, 9, 99, 29, 72, 8]))

#python3 closest_v1.py <<< "2 0 0 3 4" 5.0
#python3 closest_v1.py <<< "4 7 7 1 100 4 8 7 7" 0.0 
#python3 closest_v1.py <<< "11 4 4 -2 -2 -3 -4 -1 3 2 3 -4 0 1 1 -1 -1 3 -1 -4 2 -2 4" 1.414213
#python3 closest_v1.py <<< "11 4 4 -2 -2 -3 -4 -1 3 2 -1 -5 0 1 1 -1 -1 3 -1 -4 2 -2 4" 1.414213
#python3 closest_v1.py <<< "12 4 4 -2 -2 -3 -4 -1 3 2 3 -4 0 1 1 -1 -1 3 -1 -4 2 -2 4 4 5"
#python3 closest_v1.py <<< "2 -1000000000 -1000000000 1000000000 1000000000"