import sys
import random

def partition(starts, ends, l, r):
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

def QuickSort(starts, ends, l, r):
    
    while l < r:
        p = partition(starts, ends, l, r)
        if (p - l) < r - p:
            QuickSort(starts, ends, l, p - 1)
            l = p + 1
        else:
            QuickSort(starts, ends, p + 1, r)
            r = p - 1

def binary_search(point, starts, ends, l, r):
    if l > r: return - 1
    
    mid = l + (r - l) // 2
    if starts[mid] <= point <= ends[mid]: return mid
    elif point > ends[mid]: return binary_search(point, starts, ends, mid + 1, r)
    else: return binary_search(point, starts, ends, l, mid - 1)
    
def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    QuickSort(starts, ends, 0, len(ends) - 1)

    for p in range(len(points)):
                
        s = binary_search(points[p], starts, ends, 0, len(ends) - 1)
        if s != -1:
            cnt[p] += 1
            i = s - 1
            while i >= 0 and starts[i] <= points[p] <= ends[i]:
                cnt[p] += 1
                i -= 1
            i = s + 1
            while i < len(ends) and starts[i] <= points[p] <= ends[i]:
                cnt[p] += 1
                i += 1
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    #cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)

    for x in cnt:
        print(x, end=' ')

#python3 points_and_segments.py <<< "2 3 0 5 7 10 1 6 11"
#python3 points_and_segments.py <<< "1 3 -10 10 -100 100 0"
#python3 points_and_segments.py <<< "3 2 0 5 -3 2 7 10 1 6"
