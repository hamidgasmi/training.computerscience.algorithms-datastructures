# I. Summary:
#   1. Input, sorted arr1, arr2 of numbers
#   2. Output: return arr1 interesction arr2
#      Output  It must sorted
#   3. Constraints:
#      1. M ~ N 
#      2. M >> N
#   4. Questions:
#      Are there duplicates in the arrays? No
# II. Build my Intuition:
#   Example: arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]
#   1. Naive approch: 
#      Add all arr1 values to a arr1_set
#      For every value in arr2, check if it's in arr1_set
#      If yes, the value is a duplicate
#
#   2. To get rid of the set() data-structure:
#      Use the idea behind the merge sort: merge 2 sorted arrays
#      Keep only values that are in both arrays

class Solution:

  # Time Complexity: T = O(M + N)
  #   If M ~ N: T = O(2 * M) = O(M)
  #   If M >> N: T = O(M)
  # Space Complexity: S = O(2 * N) = O(N) in both cases
  def find_duplicates_naive(self, arr1, arr2):

    # 1. Add arr1 values to a set
    arr1_set = set()
    for val in arr1:
      arr1_set.add(val) # We assumed that there is no duplicate in arr1

    duplicates = []

    # 2. Check if arr2 values are in the set
    for val in arr2:
      if val in arr1_set:
        duplicates.append(val)

    return duplicates
  
  # Time Complexity: T(N + M)
  #   If M ~ N: T = O(M)
  #   If M >> N: T = O(M)
  # Space Complexity: S = O(N) in both cases
  def find_duplicates_2(self, arr1, arr2):

    duplicates = []

    arr1_len = len(arr1)
    arr2_len = len(arr2)

    i = 0
    j = 0
    while i < arr1_len and j < arr2_len:

      if arr1[i] == arr2[j]:
        duplicates.append(arr1[i])
        i += 1
        j += 1
      
      elif arr1[i] < arr2[j]:
        i += 1

      else:
        j += 1

    return duplicates

  # Time Complexity: T = Ω(logM) = Θ(NlogM)
  #   It's Θ instead of O because for some cases, the solution runs in less than NlogM
  #   For example, when arr1[0] > arr2 values, then the solution runs in logM
  #   let M = 2**m
  #   If M ~ N: T = Θ(MlogM): it's not efficient in this case:
  #      T(Solution 2) = O(N + M) = O(2 * 2**m)
  #      T(Solution 3) = Θ(NlogM) = Θ(NlogM) = Θ(m * 2**m)
  #      Solution 3 would be interesting in this case only when m <= 2 => N ~ M <= 4
  #   If M >> N: T = Θ(NlogM)
  #      T(Solution 2) = O(M) = O(2**m)
  #      T(Solution 3) = O(NlogM) = O(mN)
  #     It will be intersting when NlogM < M => M/logM > N
  #     For N = 2, M > 4
  #     For N = 10, M >= 64
  # Space Complexity: S = O(N + logM)
  #   logM is due to the recursive binary search: 
  def find_duplicates_binary_search(self, arr1, arr2, binary_search_func=None):

    binary_search_func = binary_search_func if binary_search_func else self._binary_search_iterative
    
    duplicates = []

    arr1_len = len(arr1)
    arr2_len = len(arr2)

    i = 0
    start = 0
    end = arr2_len - 1
    
    while i < arr1_len and start < arr2_len:
      
      start = binary_search_func(arr1[i], arr2, start, end)
      
      if start >= arr2_len:
        break
        
      elif arr1[i] == arr2[start]:
        duplicates.append(arr1[i])

        start += 1
      
      i += 1
    
    return duplicates

  def _binary_search_iterative(self, val, arr, start=0, end=None):
    end = (len(arr) - 1) if end is None else end

    arr_len = len(arr)
    assert( 0 <= start < arr_len)
    assert( 0 <= end < arr_len)

    while start < end:

      mid = (start + end) // 2

      if val == arr[mid]:
        return mid

      elif val < arr[mid]:
        end = mid - 1

      else:
        start = mid + 1        
    
    return start

  def find_duplicates_recursive_binary_search(self, arr1, arr2):

    return self.find_duplicates_binary_search(arr1, arr2, self._binary_search_recursive)

  def _binary_search_recursive(self, val, arr, start=0, end=None):
    end = (len(arr) - 1) if end is None else end
    
    if start > end:
      return start
    
    mid = (start + end) // 2
    
    if val == arr[mid]:
      return mid
    
    elif arr[mid] < val:
      return self._binary_search_recursive(val, arr, mid + 1, end)
      
    else:
      return self._binary_search_recursive(val, arr, start, mid - 1)

if __name__ == '__main__':

  solution = Solution()

  #print("Case 01: ", solution.find_duplicates_naive([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20])) # Duplicates
  #print("Case 02: ", solution.find_duplicates_naive([1, 2, 4, 5, 9], [3, 6, 7, 8, 20])) # No Duplicate
  #print("Case 03: ", solution.find_duplicates_naive([1, 2, 3, 5, 9], [3, 6, 7, 8, 20])) # 1 Duplicate
  #print("Case 04: ", solution.find_duplicates_naive([], [3, 6, 7, 8, 20])) # Empty array
  #print("Case 05: ", solution.find_duplicates_naive([1, 2, 3, 5, 9], [])) # Empty array
  #print("Case 06: ", solution.find_duplicates_naive([1, 2, 3, 5, 9], [1, 2, 3, 5, 9])) # Equal arrays
  #print("Case 07: ", solution.find_duplicates_naive([1, 2, 3, 5, 9], [1, 2, 3, 5, 6, 7, 8, 9, 20])) # Arr1 is included in Arr2
  #print("Case 08: ", solution.find_duplicates_naive([1, 2, 3, 5, 6, 7, 8, 9, 20], [1, 2, 3, 5, 9])) # Array 2 is included in Arr1
  #print("Case 09: ", solution.find_duplicates_naive([21, 22, 23, 25, 26, 27], [3, 6, 7, 8, 20])) # No duplicates arr1 values > arr2 values
  #print("Case 10: ", solution.find_duplicates_naive([3, 6, 7, 8, 20], [21, 22, 23, 25, 26, 27])) # No duplicates: arr1 values < arr2 values
  #print("Case 11: ", solution.find_duplicates_naive([10,20,30,40,50,60,70,80], [10,20,30,40,50,60])) 

  #print("Case 01: ", solution.find_duplicates_2([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20])) # Duplicates
  #print("Case 02: ", solution.find_duplicates_2([1, 2, 4, 5, 9], [3, 6, 7, 8, 20])) # No Duplicate
  #print("Case 03: ", solution.find_duplicates_2([1, 2, 3, 5, 9], [3, 6, 7, 8, 20])) # 1 Duplicate
  #print("Case 04: ", solution.find_duplicates_2([], [3, 6, 7, 8, 20])) # Empty array
  #print("Case 05: ", solution.find_duplicates_2([1, 2, 3, 5, 9], [])) # Empty array
  #print("Case 06: ", solution.find_duplicates_2([1, 2, 3, 5, 9], [1, 2, 3, 5, 9])) # Equal arrays
  #print("Case 07: ", solution.find_duplicates_2([1, 2, 3, 5, 9], [1, 2, 3, 5, 6, 7, 8, 9, 20])) # Arr1 is included in Arr2
  #print("Case 08: ", solution.find_duplicates_2([1, 2, 3, 5, 6, 7, 8, 9, 20], [1, 2, 3, 5, 9])) # Array 2 is included in Arr1
  #print("Case 09: ", solution.find_duplicates_2([21, 22, 23, 25, 26, 27], [3, 6, 7, 8, 20])) # No duplicates arr1 values > arr2 values
  #print("Case 10: ", solution.find_duplicates_2([3, 6, 7, 8, 20], [21, 22, 23, 25, 26, 27])) # No duplicates: arr1 values < arr2 values
  #print("Case 11: ", solution.find_duplicates_2([10,20,30,40,50,60,70,80], [10,20,30,40,50,60])) 

  # Iterative binary search
  #print("Case 01: ", solution.find_duplicates_binary_search([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20])) # Duplicates
  #print("Case 02: ", solution.find_duplicates_binary_search([1, 2, 4, 5, 9], [3, 6, 7, 8, 20])) # No Duplicate
  #print("Case 03: ", solution.find_duplicates_binary_search([1, 2, 3, 5, 9], [3, 6, 7, 8, 20])) # 1 Duplicate
  #print("Case 04: ", solution.find_duplicates_binary_search([], [3, 6, 7, 8, 20])) # Empty array
  #print("Case 05: ", solution.find_duplicates_binary_search([1, 2, 3, 5, 9], [])) # Empty array
  #print("Case 06: ", solution.find_duplicates_binary_search([1, 2, 3, 5, 9], [1, 2, 3, 5, 9])) # Equal arrays
  #print("Case 07: ", solution.find_duplicates_binary_search([1, 2, 3, 5, 9], [1, 2, 3, 5, 6, 7, 8, 9, 20])) # Arr1 is included in Arr2
  #print("Case 08: ", solution.find_duplicates_binary_search([1, 2, 3, 5, 6, 7, 8, 9, 20], [1, 2, 3, 5, 9])) # Array 2 is included in Arr1
  #print("Case 09: ", solution.find_duplicates_binary_search([21, 22, 23, 25, 26, 27], [3, 6, 7, 8, 20])) # No duplicates arr1 values > arr2 values
  #print("Case 10: ", solution.find_duplicates_binary_search([3, 6, 7, 8, 20], [21, 22, 23, 25, 26, 27])) # No duplicates: arr1 values < arr2 values
  #print("Case 11: ", solution.find_duplicates_binary_search([10,20,30,40,50,60,70,80], [10,20,30,40,50,60])) 

  # Recursive binary search
  print("Case 01: ", solution.find_duplicates_recursive_binary_search([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20])) # Duplicates
  print("Case 02: ", solution.find_duplicates_recursive_binary_search([1, 2, 4, 5, 9], [3, 6, 7, 8, 20])) # No Duplicate
  print("Case 03: ", solution.find_duplicates_recursive_binary_search([1, 2, 3, 5, 9], [3, 6, 7, 8, 20])) # 1 Duplicate
  print("Case 04: ", solution.find_duplicates_recursive_binary_search([], [3, 6, 7, 8, 20])) # Empty array
  print("Case 05: ", solution.find_duplicates_recursive_binary_search([1, 2, 3, 5, 9], [])) # Empty array
  print("Case 06: ", solution.find_duplicates_recursive_binary_search([1, 2, 3, 5, 9], [1, 2, 3, 5, 9])) # Equal arrays
  print("Case 07: ", solution.find_duplicates_recursive_binary_search([1, 2, 3, 5, 9], [1, 2, 3, 5, 6, 7, 8, 9, 20])) # Arr1 is included in Arr2
  print("Case 08: ", solution.find_duplicates_recursive_binary_search([1, 2, 3, 5, 6, 7, 8, 9, 20], [1, 2, 3, 5, 9])) # Array 2 is included in Arr1
  print("Case 09: ", solution.find_duplicates_recursive_binary_search([21, 22, 23, 25, 26, 27], [3, 6, 7, 8, 20])) # No duplicates arr1 values > arr2 values
  print("Case 10: ", solution.find_duplicates_recursive_binary_search([3, 6, 7, 8, 20], [21, 22, 23, 25, 26, 27])) # No duplicates: arr1 values < arr2 values
  print("Case 11: ", solution.find_duplicates_recursive_binary_search([10,20,30,40,50,60,70,80], [10,20,30,40,50,60]))





