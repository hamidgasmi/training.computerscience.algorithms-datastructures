import random
import _unit_tests_utility

class Quick_Sorts:
    
    def basic_quick_sort(self, a, left, right):
        pass

    def random_quick_sort(self, a, left, right):
        pass

    def three_ways_quick_sort(self, a, left, right):
        pass

    def recursive_tail_eliminated_quick_sort(self, a, left, right):
        pass

if __name__ == "__main__":
    
    unit_test = _unit_tests_utility.Unit_Tests_Utility()
    unit_test.get_inputs()
    a_list = unit_test.inputs[1]

    quick_sort = Quick_Sorts()

    print("Basic Quick Sort Result:", quick_sort.basic_quick_sort(a_list, 0, len(a_list)))
    print("Random Quick Sort Result:", quick_sort.random_quick_sort(a_list, 0, len(a_list)))
    print("3 Ways Quick Sort Result:", quick_sort.three_ways_quick_sort(a_list, 0, len(a_list)))
    print("Recursive Tail eliminated Quick Sort Result:", quick_sort.recursive_tail_eliminated_quick_sort(a_list, 0, len(a_list)))
    