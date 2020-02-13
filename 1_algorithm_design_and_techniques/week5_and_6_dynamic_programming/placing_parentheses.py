def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):

    
    D = []
    op = []
    for i in range(len(dataset)):
        if i % 2 == 0: 
            D.append(int(dataset[i]))
        else:
            op.append(dataset[i])

    n = len(D)
    Max = [[0 for c in range(n)] for r in range(n)]
    Min = [[0 for c in range(n)] for r in range(n)]

    for c in range(n):
        Max[c][c] = D[c]
        Min[c][c] = D[c]

    for i in range(1, n):
        for r in range(0, n - i):
            maximum = (-1) * pow(9, 14)
            minimum = pow(9, 14)
            #print("(r, c) : (" + str(r) + ", " + str(r + i) + ")")

            for j in range(i):
                #print("(" + str(r) + ", " + str(r + j) + ") op (" + str(r + j + 1) + ", " + str(r + i) + ")")

                maximum = max(maximum, 
                              evalt(Max[r][r + j], Max[r + j + 1][r + i], op[r + j]), 
                              evalt(Max[r][r + j], Min[r + j + 1][r + i], op[r + j]), 
                              evalt(Min[r][r + j], Min[r + j + 1][r + i], op[r + j]), 
                              evalt(Min[r][r + j], Max[r + j + 1][r + i], op[r + j]))
                minimum = min(minimum, 
                              evalt(Max[r][r + j], Max[r + j + 1][r + i], op[r + j]), 
                              evalt(Max[r][r + j], Min[r + j + 1][r + i], op[r + j]), 
                              evalt(Min[r][r + j], Min[r + j + 1][r + i], op[r + j]), 
                              evalt(Min[r][r + j], Max[r + j + 1][r + i], op[r + j]))
            Max[r][r + i] = maximum
            Min[r][r + i] = minimum
   
    #for r in range(n):
    #    print(Max[r])

    return Max[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))

#python3 placing_parentheses.py <<< "1+5"
#python3 placing_parentheses.py <<< "5-8+7*4-8+9"