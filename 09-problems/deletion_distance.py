import _unit_tests_utility

# Time Complexity: O(|str1| * |str2|)
# Space Complexity: O(min(|str1|, |str2|))
# dist(i, j) = min{ dist(i-1, j-1) + 0 if str1[i-1] = str2[j] else 2, dist(i-1, j)+1, dist(i, j-1) + 1 }
def deletion_distance(str1, str2):
  
  # To save more space, let's find the shorter string
  if len(str1) < len(str2):
    shorter_str = str1
    longer_str = str2
    
  else:
    shorter_str = str2
    longer_str = str1
  
  # Initialization
  cols_count = len(shorter_str) + 1
  rows_count = len(longer_str) + 1
  
  curr_distances = [col for col in range(cols_count)]
      
  # Distance calculation:
  for row in range(1, rows_count):
    
    prev_distances = curr_distances
    curr_distances = [(row if col == 0 else 0) for col in range(cols_count)]
    
    for col in range(1, cols_count):
      
      curr_distances[col] = min(prev_distances[col - 1] + (0 if shorter_str[col - 1] == longer_str[row - 1] else 2),
                                prev_distances[col] + 1,
                                curr_distances[col - 1] + 1)
      
  return curr_distances[cols_count - 1]

if __name__ == "__main__":
    unit_test = _unit_tests_utility.Unit_Tests_Utility()
    unit_test.get_inputs()

    str1 = unit_test.inputs[0]
    str2 = unit_test.inputs[1]

    print(str1, str2)

    print(deletion_distance(str1, str2))
