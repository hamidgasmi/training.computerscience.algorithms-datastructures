# Time Complexity: O(1)
# Space Complexity: O(1)
def parent(i, size):
    if i >= size:
        return -1

    return size // 2

# Time Complexity: O(1)
# Space Complexity: O(1)
def left(i, size):
    l = 2 * i + 1
    return l if l < size else -1

# Time Complexity: O(1)
# Space Complexity: O(1)
def right(i, size):
    r = 2 * i + 2
    return r if r < size else -1

# Time Complexity: O(log n)
# Space Complexity: O(1)
def siftDown(a, swaps, i, size):
    if i >= size:
        return

    minIndex = i
    l = left(i, size)
    if l != -1 and a[l] < a[minIndex]:
        minIndex = l
    r = right(i, size)
    if r != -1 and a[r] < a[minIndex]:
        minIndex = r

    if minIndex != i:
         a[i], a[minIndex] = a[minIndex], a[i]
         swaps.append((i, minIndex))
         siftDown(a, swaps, minIndex, size)

# Time Complexity: O(n)
#       Height          Nodes #    T(SiftDown)       T(BuildHeap)
#       log_2(n)          1         log_2(n)          1 * log_2(n) 
#       log_2(n) - 1      2         log_2(n) - 1      2 * [ log_2(n) - 1]
#         ...            ...         ...                 ...
#          2            ≤ n/4         2                n/4 * 2
#          1            ≤ n/2         1                n/2 * 1
#       T(BuildHeap) = n/2 * 1 + n/4 * 2 + ... + 1 * log_2(n) 
#                    = n/2 * 1 + n/4 * 2 + ... + n / 2^log_2(n) * log_2(n)
#                    = n [1/2 + 2/4 + 2/8 + ... log_2(n)/2^log_2(n)] < n * 2
#                    = O(n)
# Space Complexity: O(n)
def build_heap(data):

    size = len(data)
    swaps = []
    for i in range(parent(size - 1, size), -1, -1):
        siftDown(data, swaps, i, size)

    return swaps

# Time Complexity: O(n^2)
# Space Complexity: O(n)
def build_heap_brute(data):

    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()