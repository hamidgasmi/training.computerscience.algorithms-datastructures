import random
import _unit_tests_utility

class Quick_Sorts:
    
    def basic_quick_sort(self, a, left, right):
        if left >= right:
            return

        pivot = self.partition(a, left, right, (left + right) // 2)
        
        self.basic_quick_sort(a, left, pivot - 1)
        self.basic_quick_sort(a, pivot + 1, right)

    def random_quick_sort(self, a, left, right):
        if left >= right:
            return

        print(random.randint(left, right))
        pivot = self.partition(a, left, right, random.randint(left, right))

        self.basic_quick_sort(a, left, pivot - 1)
        self.basic_quick_sort(a, pivot + 1, right)

    def three_ways_quick_sort(self, a, left, right):
        pass

    def recursive_tail_eliminated_quick_sort(self, a, left, right):
        pass

    def partition(self, a, left, right, mid):
        assert(right < len(a))
        assert(left >= 0)
        assert(left <= mid <= right)

        self.swap(a, mid, right)

        pivot = left - 1
        for i in range(left, right):
            if a[i] <= a[right]:
                pivot += 1
                self.swap(a, pivot, i)
        pivot += 1
        self.swap(a, pivot, right)

        return pivot

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def swap(self, a, i, j):
        assert(i < len(a))
        assert(j < len(a))

        a[i] ^= a[j] # initial_a[i] Xor initial_a[j]
        a[j] ^= a[i] # initial_a[j] Xor (initial_a[i] Xor initial_a[j]) = initial_a[i]
        a[i] ^= a[j] # (initial_a[i] Xor initial_a[j]) Xor initial_a[i] = initial_a[j]

if __name__ == "__main__":
    
    unit_test = _unit_tests_utility.Unit_Tests_Utility()
    unit_test.get_inputs()
    unsorted_list = unit_test.inputs[0]

    quick_sort = Quick_Sorts()

    sorted_list = unsorted_list.copy()
    quick_sort.basic_quick_sort(sorted_list, 0, len(sorted_list) - 1)
    print("Basic Quick Sort Result:", sorted_list)

    sorted_list = unsorted_list.copy()
    quick_sort.random_quick_sort(sorted_list, 0, len(sorted_list) - 1)
    print("Random Quick Sort Result:", sorted_list)

    #sorted_list = unsorted_list.copy()
    #uick_sort.three_ways_quick_sort(sorted_list, 0, len(sorted_list) - 1)
    #print("3 Ways Quick Sort Result:", sorted_list)

    #sorted_list = unsorted_list.copy()
    #quick_sort.recursive_tail_eliminated_quick_sort(sorted_list, 0, len(sorted_list) - 1)
    #print("Recursive Tail eliminated Quick Sort Result:", sorted_list)
    