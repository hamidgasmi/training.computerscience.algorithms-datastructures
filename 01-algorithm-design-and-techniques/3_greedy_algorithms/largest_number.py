import sys
import random

def getBase(n):
    if n < 10: return 10
    elif n < 100: return 100
    elif n < 1000: return 1000
    else: return 10000

def swap(a, i, j):
    if i < 0 or i >= len(a): return
    if j < 0 or j >= len(a): return

    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def getRandomizedPartition(a, p, r):
    if r < p: return
    if r > len(a): return

    swap(a, random.randrange (p, r + 1, 1), r)
    
    i = p - 1
    for j in range(p, r):
        ar = int(a[r])
        aj = int(a[j])
        if ar * getBase(aj) + aj <= aj * getBase(ar) + ar:
            i += 1
            swap(a, i, j)
    swap(a, i + 1, r)

    return i + 1

def quickSort(a, p, r):
    if p >= r: return

    q = getRandomizedPartition(a, p, r)
    quickSort(a, p, q - 1)
    quickSort(a, q + 1, r)

def largest_number(a):
    quickSort(a, 0, len(a) - 1)

    res = ""
    for x in a:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
