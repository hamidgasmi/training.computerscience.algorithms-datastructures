import sys

def optimal_weight(W, w):

    V = [[0 for j in range(W + 1)] for i in range(len(w) + 1)]
    
    for i in range(1, len(w) + 1):
        for j in range(1, W + 1):
            V[i][j] = V[i - 1][j]
            if w[i - 1] <= j:
                val = V[i - 1][j - w[i - 1]] + w[i - 1]
                if val > V[i][j]:
                    V[i][j] = val

    return V[len(w)][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

#python3 knapsack.py <<< "10 3 1 4 8" 9
