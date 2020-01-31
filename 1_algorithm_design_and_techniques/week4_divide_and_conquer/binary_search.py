# Uses python3
import sys

def binary_search(a, x, low, high):
    if low > high: return - 1
    
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

    for x in data[n + 2:]:
        print(binary_search(a, x, 0, len(a) - 1), end = ' ')

    #python3 binary_search.py <<< "5 1 5 8 12 13 5 1 5 8 12 13"
    #python3 binary_search.py <<< "5 1 5 8 12 13 9 0 1 4 5 6 8 12 13 24"
    #python3 binary_search.py <<< "5 1 5 8 12 13 9 0 1 4 5 6 8 12 13 24"
    #python3 binary_search.py <<< "0 9 0 1 4 5 6 8 12 13 24"
    #python3 binary_search.py <<< "5 1 5 8 12 13 0"
    #python3 binary_search.py <<< "5 1 5 8 12 13 5 8 1 23 1 11"
