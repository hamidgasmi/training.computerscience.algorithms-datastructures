
import _unit_tests_utility

# Binary Search

def binary_search_recursive(a, val, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if a[mid] == val:
        return mid

    result = -1
    if a[mid] > val:
        result = binary_search_recursive(a, val, left, mid - 1)
        
    else:
        result = binary_search_recursive(a, val, mid + 1, right)
    
    return mid if result == -1 else result

def binary_search_iterative(a, val):
    
    left = 0
    right = len(a) - 1

    result = -1
    while (left <= right):

        mid = (left + right) // 2
        if a[mid] == val:
            result = mid
            break

        if a[mid] > val:
            right = mid - 1

        else:
            left = mid + 1    
        
        result = mid
    
    return result

if __name__ == "__main__":

    unit_test = _unit_tests_utility.Unit_Tests_Utility()
    unit_test.get_inputs()

    a_val = unit_test.inputs[0][0]
    a_list = unit_test.inputs[1]

    print("(Iterative, Recursive) :", binary_search_iterative(a_list, a_val), binary_search_recursive(a_list, a_val, 0, len(a_list) - 1))