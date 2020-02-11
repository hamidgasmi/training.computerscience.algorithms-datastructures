import sys

def lcs3(a1, a2, a3):

    D = [[[0 for d in range(len(a3) + 1)] for c in range(len(a2) + 1)] for r in range(len(a1) + 1)]

    for r in range(1, len(a1) + 1):
        D[r][0][0] = 0
    for c in range(1, len(a2) + 1):
        D[0][c][0] = 0
    for d in range(1, len(a3) + 1):
        D[0][0][d] = 0
    
    for r in range(1, len(a1) + 1):
        for c in range(1, len(a2) + 1):
            for d in range(1, len(a3) + 1):
            
                if a1[r - 1] == a2[c - 1] == a3[d - 1]:
                    D[r][c][d] = max(D[r - 1][c - 1][d - 1] + 1,
                                     D[r][c - 1][d - 1], D[r][c - 1][d], D[r][c][d - 1],
                                     D[r - 1][c][d - 1], D[r - 1][c][d], D[r - 1][c][d - 1],
                                     D[r - 1][c - 1][d], D[r - 1][c][d], D[r - 1][c - 1][d])
                else:
                    D[r][c][d] = max(D[r - 1][c - 1][d - 1],
                                     D[r][c - 1][d - 1], D[r][c - 1][d], D[r][c][d - 1],
                                     D[r - 1][c][d - 1], D[r - 1][c][d], D[r - 1][c][d - 1],
                                     D[r - 1][c - 1][d], D[r - 1][c][d], D[r - 1][c - 1][d])

    return D[len(a1)][len(a2)][len(a3)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))

#python3 lcs3.py <<< "3 1 2 3 3 2 1 3 3 1 3 5" 2
#python3 lcs3.py <<< "5 8 3 2 1 7 7 8 2 1 3 8 10 7 6 6 8 3 1 4 7" 3