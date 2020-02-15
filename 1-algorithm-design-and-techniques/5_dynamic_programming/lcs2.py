#Uses python3
import sys

def lcs2(a, b):
    
    D = [[0 for c in range(len(a) + 1)] for r in range(len(b) + 1)] 
    for c in range(1, len(a) + 1):
        D[0][c] = 0
    for r in range(1, len(b) + 1):
        D[r][0] = 0

    for c in range(1, len(a) + 1):
        for r in range(1, len(b) + 1):
            
            if a[c - 1] == b[r - 1]:
                D[r][c] = max(D[r - 1][c - 1] + 1, D[r][c - 1], D[r - 1][c])
            else:
                D[r][c] = max(D[r - 1][c - 1], D[r][c - 1], D[r - 1][c])

    for r in range(len(b) + 1):
        print(D[r])

    return D[len(b)][len(a)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

#python3 lcs2.py <<< "3 2 7 5 2 2 5"
#python3 lcs2.py <<< "1 7 4 1 2 3 4"
#python3 lcs2.py <<< "4 2 7 8 3 4 5 2 8 7"

