# Uses python3
# O(n^2)
def maxPairwiseProductNaiveApproach(aList):
    
    result = 0
    for i in range(0, len(aList)):
        for j in range(i+1, len(aList)):
            if aList[i]*aList[j] > result:
                result = aList[i]*aList[j]
    return result

# O(n): Max pairwise product is equal to the product of the list's 2 highest numbers
def maxPairwiseProduct(aList):
    
    if len(aList) < 2: return 0

    max1 = aList[0] if aList[0] <= aList[1] else aList[1]
    max2 = aList[1] if aList[0] <= aList[1] else aList[0]
    for i in range(2, len(aList)):
        if aList[i] >= max2:
            max1 = max2
            max2 = aList[i]
        elif aList[i] > max1 and aList[i] < max2:
            max1 = aList[i]

    return max1 * max2

n = int(input("Enter the number of integer items: "))
print("Enter now " + str(n) + " integers separated by a space:")
a = [int(x) for x in input().split()]
assert(len(a) == n)
#print("The max pairwise product is: ", maxPairwiseProductNaiveApproach(a))
print("The max pairwise product is: ", maxPairwiseProduct(a))