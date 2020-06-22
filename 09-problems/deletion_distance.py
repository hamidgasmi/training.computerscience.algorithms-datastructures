import utility_devel

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
    unit_test = utility_devel.Unit_Tests_Utility()
    unit_test.get_inputs()

    str1 = unit_test.inputs[0]
    str2 = unit_test.inputs[1]

    print(str1, str2)

    print(deletion_distance(str1, str2))


#Base case:
#    "HEAT", ""
#    In this case the deletion distance is simply the length of the other string

#Simple case: when a string is containing the other string
#    "HEAT", "HEA"
#    _  _  H  E  A  T
#    _  0  1  2  3  4
#    H  1  0  1  2  3 
#    E  2  1  0  1  2
#    A  3  2  1  0  1

#Order:
#    ab, ba

#Recursive relation:
#    Do you see a recursive relation between the deletionDistance(str1, str2), and the deletionDistance for some prefixes of str1 and str2
#    HEAT, HEA
#    dist(i, j) = min{dist(i-1, j-1) + 0 if str1[i-1] = str2[j] else 2, dist(i-1, j)+1, dist(i, j-1) + 1}
#    _  _  H  E  A  T
#    _  0  1  2  3  4
#    E  1  2  1  2  3
#    A  2  3  2  1  2
#    T  3  4  3  2  1

#    _  _  H  E  A  T
#    _  0  1  2  3  4
#    H  1  0  1  2  3
#    E  2  1  0  1  2
#    A  3  2  1  0  1
#    P  4  3  2  1  2

#Dynamic Programmning:

#Time Complexity
#Space Complexity
