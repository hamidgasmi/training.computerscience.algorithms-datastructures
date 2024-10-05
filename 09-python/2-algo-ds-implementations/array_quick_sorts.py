import random
import utility_devel

# It's solved with a divide-and-conquer approach
# It is implemented 4 different way:
#    1. Basic Quick Sort uses the "right" as a pivot
#       Running time: 
#           O(|a| log |a|) when the partitions are balanced
#           O(|a|**2) when the partitions are unbalanced: one of the partition size is: n - 1
#       Space complexity:
#           O(log |a|) when the partitions are balanced
#           O(|a|) when the partitions are unbalanced: one of the partition size is: n - 1
#
#   2. Random Quick Sort: uses a random value between "left" and "right" as a pivot
#      It addresses the worst case of the basic quick sort, above
#      It allows to get balanced partition in average
#      Running Time: 
#           Average: O(|a| log |a|)
#           Worst case: O(|a|**2) when all list items are equal
#      Space Complexity: 
#           Average: O(log |a|)
#           Worst case: O(|a|) 
#
#   3. 3 ways partitions:
#      It addresses the case where there're duplicate values in the list
#      It's done by partitionning our list into 3 partitions: [left, left_pivot[, [left_pivot, right_pivot], ]right_pivot, right]
#      All the values in the range [left_pivot, right_pivot] are equal
#      Running Time: Average: O(|a| log |a|)
#      Space Complexity: Average: O(log |a|)
#
#   4. Recursive tail elimination:
#      It addresses the issue related to space complexity
#      It allows to avoid the deepest recursive call
#      Space Complexity: O(log |a|) for all cases

class Quick_Sorts:
        
    def basic_quick_sort(self, a, left=0, right=None):
        if right is None:
            right = len(a) - 1
        
        if left >= right:
            return

        piv_pos = right
        pivot = self._two_partition(a, left, right, piv_pos)
        
        self.basic_quick_sort(a, left, pivot - 1)
        self.basic_quick_sort(a, pivot + 1, right)
    
    def random_quick_sort(self, a, left=0, right=None):
        if right is None:
            right = len(a) - 1
        
        if left >= right:
            return
        
        piv_pos = random.randint(left, right)
        pivot = self._two_partition(a, left, right, piv_pos)

        self.random_quick_sort(a, left, pivot - 1)
        self.random_quick_sort(a, pivot + 1, right)

    def _two_partition(self, a, left, right, piv_pos):
        assert(right < len(a))
        assert(left >= 0)
        assert(left <= piv_pos <= right)

        self._swap(a, piv_pos, right)

        pivot = left - 1
        for i in range(left, right):
            if a[i] <= a[right]:
                pivot += 1
                self._swap(a, pivot, i)
        pivot += 1
        self._swap(a, pivot, right)

        return pivot

    def recursive_tail_eliminated_quick_sort(self, a, left=0, right=None):
        if right is None:
            right = len(a) - 1
        
        while left < right:
            
            piv_pos = random.randint(left, right)
            (left_piv, right_piv) = self._three_partitions(a, left, right, piv_pos)

            if (left_piv - left) < (right - right_piv):
                self.recursive_tail_eliminated_quick_sort(a, left, left_piv - 1)
                left = right_piv + 1

            else:
                self.recursive_tail_eliminated_quick_sort(a, right_piv + 1, right)
                right = left_piv - 1

    def three_ways_quick_sort(self, a, left=0, right=None):
        if right is None:
            right = len(a) - 1
        
        if left >= right:
            return
        
        piv_pos = random.randint(left, right)
        (pivot_left, pivot_right) = self._three_partitions(a, left, right, piv_pos)
        
        self.three_ways_quick_sort(a, left, pivot_left - 1)
        self.three_ways_quick_sort(a, pivot_right + 1, right)
        
    def _three_partitions(self, a, left, right, piv_pos):
        assert(right < len(a))
        assert(left >= 0)
        assert(left <= piv_pos <= right)

        self._swap(a, piv_pos, right)
        
        left_piv = left - 1
        right_piv = right

        i = left
        while i < right_piv:
            
            if a[i] < a[right]:
                left_piv += 1
                self._swap(a, left_piv, i)

            if a[i] == a[right]:
                # I should move to the end of the list: I shouldn't increment i in this case
                right_piv -= 1
                self._swap(a, i, right_piv)

            else:
                i += 1
        
        # Move pivot range to the middle of the list
        left_piv += 1
        self._swap(a, left_piv, right_piv)
        
        i = right_piv
        right_piv = left_piv
        while i < right:
            right_piv += 1
            i += 1
            self._swap(a, right_piv, i)
            
        
        return (left_piv, right_piv)
    
    def _swap(self, a, i, j):
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
    def _swap_xor(self, a, i, j):
        assert(i < len(a))
        assert(j < len(a))

        if i == j:
            return

        a[i] ^= a[j] # initial_a[i] Xor initial_a[j]
        a[j] ^= a[i] # initial_a[j] Xor (initial_a[i] Xor initial_a[j]) = initial_a[i]
        a[i] ^= a[j] # (initial_a[i] Xor initial_a[j]) Xor initial_a[i] = initial_a[j]

if __name__ == "__main__":
    
    #unit_test = utility_devel.Unit_Tests_Utility()
    #unit_test.get_inputs()
    #unsorted_list = unit_test.inputs[0]
    unsorted_list = [6, 8, 2]
    print("Input: ", unsorted_list)

    quick_sort = Quick_Sorts()

    sorted_list = unsorted_list.copy()
    quick_sort.basic_quick_sort(sorted_list)
    print("Basic Quick Sort Output:", sorted_list)

    sorted_list = unsorted_list.copy()
    quick_sort.random_quick_sort(sorted_list)
    print("Random Quick Sort Output:", sorted_list)

    sorted_list = unsorted_list.copy()
    quick_sort.three_ways_quick_sort(sorted_list)
    print("3 Ways Quick Sort Output:", sorted_list)

    sorted_list = unsorted_list.copy()
    quick_sort.recursive_tail_eliminated_quick_sort(sorted_list)
    print("Recursive Tail eliminated Quick Sort Output:", sorted_list)
    