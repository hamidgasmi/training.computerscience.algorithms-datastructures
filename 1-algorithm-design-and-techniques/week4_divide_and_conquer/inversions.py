import sys

def Merge(a, b, left, mid, right):
    l = left
    r = mid + 1
    i = left
    inversions = 0
    while l <= mid and r <= right: 
        if a[l] <= a[r]:
            b[i] = a[l]
            l += 1
        else:
            #if a[l] > a[r] => a[l + 1] > a[r] ... a[mid] > a[r]
            b[i] = a[r]
            r += 1
            inversions += 1 * (mid - l + 1)
        i += 1

    while l <= mid:
        b[i] = a[l]
        l += 1
        i += 1
    
    while r <= right:
        b[i] = a[r]
        r += 1
        i += 1

    for i in range(left, right + 1):
        a[i] = b[i]

    return inversions

#T(n) = 2 T(n / 2) + c * n
#T(n) = O(n log n)
def get_number_of_inversions(a, b, left, right):
    if left >= right:
        return 0

    number_of_inversions = 0

    mid = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, mid)
    number_of_inversions += get_number_of_inversions(a, b, mid + 1, right)
    
    number_of_inversions += Merge(a, b, left, mid, right)

    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a) - 1))

#python3 inversions.py <<< "0"
#python3 inversions.py <<< "1 1"
#python3 inversions.py <<< "2 1 2"
#python3 inversions.py <<< "2 2 1"
#python3 inversions.py <<< "5 2 3 9 2 9"
#python3 inversions.py <<< "5 3 2 9 3 3"
#python3 inversions.py <<< "5 3 2 9 3 9"
#python3 inversions.py <<< "5 2 9 2 2 9"
#python3 inversions.py <<< "6 3 2 9 3 3 3"
#python3 inversions.py <<< "6 3 2 9 3 3 2"
#python3 inversions.py <<< "6 3 2 9 3 3 9"
#python3 inversions.py <<< "6 2 3 9 2 3 9"
#python3 inversions.py <<< "9 2 3 9 2 3 9 9 3 2"
#python3 inversions.py <<< "19 1 4 2 4 2 4 1 2 4 1 2 2 2 2 4 1 4 4 4"