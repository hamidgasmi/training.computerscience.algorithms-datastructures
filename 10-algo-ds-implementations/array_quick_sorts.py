import random
import _unit_tests_utility

class Quick_Sorts:
    
    def basic_quick_sort(self, a, left, right):
        if left >= right:
            return

        pivot = self.two_partition(a, left, right, right)
        
        self.basic_quick_sort(a, left, pivot - 1)
        self.basic_quick_sort(a, pivot + 1, right)

    def random_quick_sort(self, a, left, right):
        if left >= right:
            return

        pivot = self.two_partition(a, left, right, random.randint(left, right))

        self.basic_quick_sort(a, left, pivot - 1)
        self.basic_quick_sort(a, pivot + 1, right)

    def two_partition(self, a, left, right, p):
        assert(right < len(a))
        assert(left >= 0)
        assert(left <= p <= right)

        self.swap(a, p, right)

        pivot = left - 1
        for i in range(left, right):
            if a[i] <= a[right]:
                pivot += 1
                self.swap(a, pivot, i)
        pivot += 1
        self.swap(a, pivot, right)

        return pivot

    def recursive_tail_eliminated_quick_sort(self, a, left, right):
        assert(left < len(a))
        assert(right < len(a))


    def three_ways_quick_sort(self, a, left, right):
        
        if left >= right:
            return
        
        (pivot_left, pivot_right) = self.three_partition(a, left, right, right) #random.randint(left, right))
        
        self.three_ways_quick_sort(a, left, pivot_left - 1)
        self.three_ways_quick_sort(a, pivot_right + 1, right)
        
    def three_partition(self, a, left, right, p):
        assert(right < len(a))
        assert(left >= 0)
        assert(left <= p <= right)

        self.swap(a, p, right)
        
        pivot_left = left - 1
        pivot_right = right

        i = left
        while i < pivot_right:
            
            if a[i] < a[right]:
                pivot_left += 1
                self.swap(a, pivot_left, i)

            if a[i] == a[right]:
                pivot_right -= 1
                self.swap(a, i, pivot_right)

            else:
                i += 1
        
        # Move pivot range to the middle of the list
        pivot_left += 1
        self.swap(a, pivot_left, pivot_right)
        
        i = pivot_right + 1
        pivot_right = pivot_left
        while i <= right:
            pivot_right += 1
            self.swap(a, pivot_right, i)
            i += 1
        
        return (pivot_left, pivot_right)
    
    def swap(self, a, i, j):
        assert(i < len(a))
        assert(j < len(a))

        if i == j:
            return

        initial_a_i = a[i]
        a[i] = a[j]
        a[j] = initial_a_i

    # Time Complexity: O(1)
    # Space Complexity: O(1) (In place)
    # It doesn't work with floats nor strings
    def swap_xor(self, a, i, j):
        assert(i < len(a))
        assert(j < len(a))

        if i == j:
            return

        a[i] ^= a[j] # initial_a[i] Xor initial_a[j]
        a[j] ^= a[i] # initial_a[j] Xor (initial_a[i] Xor initial_a[j]) = initial_a[i]
        a[i] ^= a[j] # (initial_a[i] Xor initial_a[j]) Xor initial_a[i] = initial_a[j]

if __name__ == "__main__":
    
    unit_test = _unit_tests_utility.Unit_Tests_Utility()
    unit_test.get_inputs()
    unsorted_list = unit_test.inputs[0]
    print("Input: ", unsorted_list)

    quick_sort = Quick_Sorts()

    sorted_list = unsorted_list.copy()
    quick_sort.basic_quick_sort(sorted_list, 0, len(sorted_list) - 1)
    print("Basic Quick Sort Output:", sorted_list)

    sorted_list = unsorted_list.copy()
    quick_sort.random_quick_sort(sorted_list, 0, len(sorted_list) - 1)
    print("Random Quick Sort Output:", sorted_list)

    sorted_list = unsorted_list.copy()
    quick_sort.three_ways_quick_sort(sorted_list, 0, len(sorted_list) - 1)
    print("3 Ways Quick Sort Output:", sorted_list)

    #sorted_list = unsorted_list.copy()
    #quick_sort.recursive_tail_eliminated_quick_sort(sorted_list, 0, len(sorted_list) - 1)
    #print("Recursive Tail eliminated Quick Sort Output:", sorted_list)
    