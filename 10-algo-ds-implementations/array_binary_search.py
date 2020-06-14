
import _unit_tests_utility

# Binary Search
# Input: a sorted list (a), a value to serach for (val)
# Output: An integer that could be greater than the list length
#         If "val" exists in the list, the functions return its position (the 1st. position found)
#         If "val" doesn't exist, the functions return the position where it should be inserted 
# Analysis:
#    - It uses Divide-and-Conquer technic
#    - Time complexity: T(n) = O(c log |a|)
#           c is the running time to compare val to an item of the list
#           |a| is the list length
#           E.g. 1. For integer, c = O(1) ==> T(n) = O(log |a|)
#           E.g. 2. For strings, c = O(|val|) ==> T(n) = O(|val| log |a|)
#    - Space complexity: 
#          - Recursive version: O(log |a|)
#          - Iterative version: O(1)

def binary_search_recursive(a, val, left, right):
    if left > right:
        # The value doesn't exist, it would fit in the position "left"
        return left

    mid = (left + right) // 2
    if a[mid] == val:
        return mid

    result = 0
    if a[mid] > val:
        result = binary_search_recursive(a, val, left, mid - 1)
        
    else:
        result = binary_search_recursive(a, val, mid + 1, right)
    
    return result

def binary_search_iterative(a, val):
    
    left = 0
    right = len(a) - 1

    result = left
    while (left <= right):

        mid = (left + right) // 2
        if a[mid] == val:
            result = mid
            break

        if a[mid] > val:
            right = mid - 1

        else:
            left = mid + 1    
        
        result = left
    
    return result

if __name__ == "__main__":

    unit_test = _unit_tests_utility.Unit_Tests_Utility()
    unit_test.get_inputs()

    a_val = unit_test.inputs[0][0]
    a_list = unit_test.inputs[1]

    print("(Iterative , Recursive) : (", binary_search_iterative(a_list, a_val), " , ", 
                                         binary_search_recursive(a_list, a_val, 0, len(a_list) - 1), ")", sep = "")