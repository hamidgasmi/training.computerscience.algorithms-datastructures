import sys

def copyArray(arr, p, r):
    if p >= len(arr): return []
    if r >= len(arr): r = len(arr) - 1

    subArr = [0] * (r - p + 1)
    for i in range(p, r + 1):
        subArr[i - p] = arr[i]

    return subArr

def mergeSortedPartitions(w, v, p, q, r):

    LeftW = copyArray(w, p, q)
    RightW = copyArray(w, q + 1, r)

    LeftV = copyArray(v, p, q)
    RightV = copyArray(v, q + 1, r)  

    i = j = 0 
    k = p
    while i < len(LeftV) and j < len(RightV):
        if RightW[j] == 0 or (LeftW[i] != 0 and LeftV[i] / LeftW[i] >= RightV[j] / RightW[j]):
            v[k] = LeftV[i]
            w[k] = LeftW[i]
            i += 1
        else:
            v[k] = RightV[j]
            w[k] = RightW[j]
            j += 1
        k += 1

    #Copy the remaining items
    while i < len(LeftV):
        v[k] = LeftV[i]
        w[k] = LeftW[i]
        i += 1
        k += 1

    while j < len(RightV):
        v[k] = RightV[j]
        w[k] = RightW[j]
        j += 1
        k += 1

def mergeSort(w, v, p, r):
    if (p >= r): return

    q = (p + r) // 2
    mergeSort(w, v, p, q)
    mergeSort(w, v, q + 1, r)
    mergeSortedPartitions(w, v, p, q, r)

def get_optimal_value(capacity, weights, values):
    
    if capacity == 0: return 0
    if len(weights) != len(values): return 0
    
    #Sort wights and values based on the unit value
    mergeSort(weights, values, 0, len(values) - 1)

    i = 0 
    value = 0.0000
    while capacity > 0 and i < len(values):
        if weights[i] > 0:
            takenWeight = min(capacity, weights[i])
            takenValue = values[i] * takenWeight / weights[i]
            
            value = value + takenValue
            capacity = capacity - takenWeight

            values[i] = values[i] - takenValue
            weights[i] = weights[i] - takenWeight

        i += 1

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

    #"5 50 60 20 100 50 120 30 115 22 122 27"
    #"5 50 60 20 100 50 115 22 122 27 120 30"
    #"5 50 60 10 100 5 12 7 115 11 122 13"
    #"3 50 60 20 100 50 120 30"
    #"3 50 60 0 100 50 120 30"
    #"3 50 60 0 100 0 120 0"
    #1 10 500 30
    #"5 50 60 20 60 20 60 20 60 20 60 20"
    #print(values)
    #print(weights)
    #print(copySubArray(weights, 0, -1))
    #mergeSortedPartitions(weights, values, 3, 3, 4)
    #mergeSort(weights, values, 0, len(values) - 1)
    #print(values)
    #print(weights)


    