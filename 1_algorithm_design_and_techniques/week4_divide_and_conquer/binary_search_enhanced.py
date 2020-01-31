# Uses python3
import sys
import random

def swap(b, mapInitB, i, j):
    if i < 0 or i >= len(b): return
    if j < 0 or j >= len(b): return

    aVal = b[i]
    aPos = mapInitB[i]

    b[i] = b[j]
    mapInitB[i] = mapInitB[j]

    b[j] = aVal
    mapInitB[j] = aPos

def getRandomizedPartition(b, mapInitB, low, high):
    if high < low: return
    if high > len(b): return

    swap(b, mapInitB, random.randrange (low, high + 1, 1), high)
    
    i = low - 1
    for j in range(low, high):
        if (b[j] <= b[high]):
            i += 1
            swap(b, mapInitB, i, j)
    swap(b, mapInitB, i + 1, high)

    return i + 1

def quickSort(b, mapInitB, low, high):
    if low >= high: return

    r = getRandomizedPartition(b, mapInitB, low, high)
    quickSort(b, mapInitB, low, r - 1)
    quickSort(b, mapInitB, r + 1, high)

def binary_search(a, x, low, high):
    if low > high: return low - 1
    elif a[low] == x: return low
    
    mid = low + (high - low) // 2
    if a[mid] == x: return mid
    elif a[mid] < x: return binary_search(a, x, mid + 1, high)
    else: return binary_search(a, x, low, mid - 1)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    b = data[n + 2:]

    #Sort b by keeping its initial positions: O(b log b)
    mapInitB = [0] * len(b)
    for i in range(len(b)): mapInitB[i] = i
    quickSort(b, mapInitB, 0, len(b) - 1)

    result = [0] * len(b)
    low = 0
    high = len(a) - 1
    for i in range(len(b)): #O(n)
        low = binary_search(a, b[i], low, high)
        #Insert the result for Bi in Bi initial position
        result[mapInitB[i]] = low
        low = max(0, low)
    print(result)

    #print(binary_search(a, x, 0, len(a) - 1), end = ' ')
    #python3 binary_search.py <<< "5 1 5 8 12 13 5 1 5 8 12 13"
    #python3 binary_search.py <<< "5 1 5 8 12 13 9 0 1 4 5 6 8 12 13 24"
    #python3 binary_search.py <<< "5 1 5 8 12 13 9 0 1 4 5 6 8 12 13 24"
    #python3 binary_search.py <<< "0 9 0 1 4 5 6 8 12 13 24"
    #python3 binary_search.py <<< "5 1 5 8 12 13 0"
    #python3 binary_search.py <<< "5 1 5 8 12 13 5 8 1 23 1 11"
