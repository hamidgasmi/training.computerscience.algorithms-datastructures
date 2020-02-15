import sys
import random

def partition3Way(a, l, r, m):

    j = random.randint(l, r)
    a[r], a[j] = a[j], a[r]

    m1 = l - 1
    m2 = r
    while m2 - 1 >= 0 and a[m2 - 1] == a[r]:
        m2 -= 1

    j = l
    while j >= l and j < m2:
        if a[j] == a[r]:
            m2 -= 1
            a[j], a[m2] = a[m2], a[j]
        elif a[j] < a[r]:
            m1 += 1
            a[m1], a[j] = a[j], a[m1]
            j += 1
        else: j += 1

    k = m1
    for j in range(m2, r + 1):
        k += 1
        a[j], a[k] = a[k], a[j]

    m[0], m[1] = m1 + 1, k
    
def randomized3WayQuickSort(a, l, r):
    if l >= r:
        return
    
    m = [-1] * 2
    partition3Way(a, l, r, m)
    randomized3WayQuickSort(a, l, m[0] - 1)
    randomized3WayQuickSort(a, m[1] + 1, r)

#Tail Recursion Eliminated
def randomized3WayQuickSortOptimized(a, l, r):
    while l < r:
        m = [-1] * 2
        partition3Way(a, l, r, m)
        if m[0] - l < r - m[1]:
            randomized3WayQuickSortOptimized(a, l, m[0] - 1)
            l = m[1] + 1
        else:
            randomized3WayQuickSortOptimized(a, m[1] + 1, r)
            r = m[0] - 1

def areEqual(arr1, arr2, n, m): 
    if (n != m): 
        return False

    # Linearly compare elements 
    for i in range(0, n): 
        if (arr1[i] != arr2[i]):
            return False
  
    return True
  
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = a.copy()
    c = a.copy()

    randomized3WayQuickSort(a, 0, n - 1)
    randomized3WayQuickSortOptimized(b, 0, n - 1)
    randomized_quick_sort(c, 0, n - 1)

    assert(areEqual(a, c, n, n))
    assert(areEqual(a, b, n, n))

#python3 quick-sort_3-ways-partition.py <<< "5 3 2 9 3 3"
#python3 quick-sort_3-ways-partition.py <<< "5 3 2 9 3 9"
#python3 quick-sort_3-ways-partition.py <<< "5 2 9 2 2 9"
#python3 quick-sort_3-ways-partition.py <<< "6 3 2 9 3 3 3"
#python3 quick-sort_3-ways-partition.py <<< "6 3 2 9 3 3 2"
#python3 quick-sort_3-ways-partition.py <<< "6 3 2 9 3 3 9"
#python3 quick-sort_3-ways-partition.py <<< "6 2 3 9 2 3 9"
#python3 quick-sort_3-ways-partition.py <<< "9 2 3 9 2 3 9 9 3 2"
#python3 quick-sort_3-ways-partition.py <<< "19 1 4 2 4 2 4 1 2 4 1 2 2 2 2 4 1 4 4 4"