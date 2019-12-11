# O(n^2)
def maxPairwiseProductNaiveApproach(n, aList):
    result = 0

    for i in range(0, n):
        for j in range(i+1, n):
            if aList[i]*aList[j] > result:
                result = aList[i]*aList[j]
    return result


n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)
print(maxPairwiseProductNaiveApproach(n, a))