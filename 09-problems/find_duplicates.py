# 1. Input, sorted arr1, arr2 of numbers
# 2. Output: return arr1 interesction arr2
#    Output must sorted
# Constraints:
# 1. M = N 
# 2. M >> N
# Solution:
# 


def find_duplicates(arr1, arr2):
  
  arr1_len = len(arr1)
  
  i = 0
  start = 0
  end = len(arr2) - 1
  duplicates = []
  while (i < arr1_len): #To what if the last value of arry1 isn't in arry2
    
    if binary_search(arr2, arr1[i], start, end) != -1:
      duplicates.append(arr1[i])
      
    i += 1
    
  return duplicates
  
def binary_search(arr, val, start, end):
  if start > end:
    return -1
    
  mid = (start + end) // 2
  
  if val == arr[mid]:
    return mid
  
  if arr[mid] < val:
    return binary_search(arr, val, mid + 1, end)
    
  else:
    return binary_search(arr, val, start, mid - 1)
    
print(find_duplicates([10,20,30,40,50,60,70,80], [10,20,30,40,50,60]))
#print(binary_search([3, 6, 8, 20], 7, 0, 3))
# 
# [1, 2, 3], [6, 7, 5, 8, 20]
# Case: last item (arr1) is 1st value in arr2: O(log M)
# Case: last item (arr1) is at pos p O(N log M 



