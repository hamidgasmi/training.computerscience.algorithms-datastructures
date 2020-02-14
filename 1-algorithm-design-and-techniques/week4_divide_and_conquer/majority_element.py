import sys

def getStrictMajorityOccurence(left, right):

    return (right - left + 1) // 2 + 1

def getOccurence(a, m, left, right):

    occurence = 0
    for i in range(left, right + 1):
        if a[i] == m: occurence += 1

    return occurence

# T(n) = 2 T(n/2) + 2 n
# O(n log n) 
def get_majority_element(a, left, right):
    if left > right:
        return -1
    if left == right:
        return a[left]

    if left + 1 == right:
        if a[left] == a[right]:
            return a[left]
        else: return -1
    
    mid = left + (right - left) // 2
    leftMajority = get_majority_element(a, left,  mid)
    rightMajority = get_majority_element(a, mid + 1, right)

    if leftMajority == rightMajority: return leftMajority
    
    strictMajority = getStrictMajorityOccurence(left, right)
    if leftMajority != -1:
        occurence = getOccurence(a, leftMajority, mid + 1, right)
        if getStrictMajorityOccurence(left, mid) + occurence >=  strictMajority : return leftMajority
        occurence += getOccurence(a, leftMajority, left,  mid)
        if occurence >= strictMajority: return leftMajority
    
    if rightMajority != -1:
        occurence = getOccurence(a, rightMajority, left,  mid)
        if getStrictMajorityOccurence(mid + 1, right) + occurence >= strictMajority: return rightMajority
        occurence += getOccurence(a, rightMajority, mid + 1, right)
        if occurence >= strictMajority: return rightMajority

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n - 1) != -1:
        print(1)
    else:
        print(0)

#python3 majority_element.py <<< "5 2 3 9 2 2"
#python3 majority_element.py <<< "4 1 2 3 4"
#python3 majority_element.py <<< "4 1 2 3 1"
#python3 majority_element.py <<< "8 2 2 1 2 1 1 1 1"
#python3 majority_element.py <<< "10 512766168 717383758 5 126144732 5 573799007 5 5 5 405079772"
#python3 majority_element.py <<< "10 1 2 5 3 5 4 5 5 5 6"