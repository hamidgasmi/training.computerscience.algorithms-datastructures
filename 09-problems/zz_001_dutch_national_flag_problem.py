"""
    1. Problem Summary / Clarifications / TDD:
        Input: [1, 0, 2, 1, 0]
        Output: [0 0 1 1 2]

        Input: [2, 2, 0, 1, 2, 0]
        Output: [0 0 1 2 2 2 ]
    
    2. Intuition:
        - To use two pointers: 
            left for 0s
            right for 2s
        - For each element in the array:
            - If it's equal to 0, swap with left
            - if it's equal to 2, swap with right
    
    3. Complexity Analysis:
        Time Complexity: O(|arr|)
        Space Complexity: O(1)

"""

def dutch_flag_sort(arr):
  
  i = 0
  l = 0
  r = len(arr) - 1
  while i <= r:
    
    if arr[i] == 0:      
      arr[l], arr[i] = arr[i], arr[l]
      l += 1
      i += 1

    elif arr[i] == 2:
      arr[i], arr[r] = arr[r], arr[i]
      r -= 1

    else:
      print(i, arr)
      i += 1

  return arr