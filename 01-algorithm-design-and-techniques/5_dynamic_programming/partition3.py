import sys

def get_total_value(A):
    total_value = 0
    for i in range(len(A)):
        total_value += A[i]

    return total_value

def optimal_values(W, w):

    V1 = [[0 for j in range(W + 1)] for i in range(len(w) + 1)]
    V2 = [[0 for j in range(W + 1)] for i in range(len(w) + 1)]
    
    for i in range(1, len(w) + 1):
        for j in range(1, W + 1):
            V1[i][j] = V1[i - 1][j]
            V2[i][j] = V2[i - 1][j]
            if w[i - 1] <= j:
                val1 = V1[i - 1][j - w[i - 1]] + w[i - 1]
                val2 = V2[i - 1][j - w[i - 1]] + w[i - 1]
                if val1 > V1[i][j]:
                    V1[i][j] = val1
                elif val2 > V2[i][j]:
                    V2[i][j] = val2

    if V1[len(w)][W] == V2[len(w)][W] == W: 
        return 1
    
    return 0

def partition3(A):
    if len(A) < 3: return 0

    #O(A)
    total_value = get_total_value(A)
    if total_value % 3 != 0: return 0
    desired_value = total_value // 3

    return optimal_values(desired_value, A)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

#python3 partition3.py <<< "1 30"
#python3 partition3.py <<< "2 30 30"
#python3 partition3.py <<< "3 30 30 30"
#python3 partition3.py <<< "4 3 3 3 3"
#python3 partition3.py <<< "4 3 3 3 3"
#python3 partition3.py <<< "13 1 2 3 4 5 5 7 7 8 10 12 19 25"
