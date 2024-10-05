#import utility_devel

class Merge_Sort:

    # Running Time: O(c |a| log |a|)
    #    c is the necessary time required to compare 2 items in a
    #    For integers, c = O(1)
    #    For strings, c = max(|a[i]|) for i >= 0 and i < |a|
    # Space complexity: O(c |a|)
    #    For integers, c = O(1)
    #    For strings, c = max(|a[i]|) for i >= 0 and i < |a|
    def merge_sort(self, a, left=0, right=None):
        if right is None:
            right = len(a) - 1

        if left >= right:
            return
        
        mid = (left + right) // 2
        self.merge_sort(a, left, mid)
        self.merge_sort(a, mid + 1, right)

        self._merge_sorted_partitions(a, left, mid, right)

    def _merge_sorted_partitions(self, a, left, mid, right):
        
        tmp_a = [ a[i] for i in range(left, right + 1) ]
        
        i = left
        l = left
        r = mid + 1

        while l <= mid and r <= right:
            if tmp_a[l - left] <= tmp_a[r - left]:
                a[i] = tmp_a[l - left]
                l += 1

            else:
                a[i] = tmp_a[r - left]
                r += 1
            
            i += 1
        
        while l <= mid:
            a[i] = tmp_a[l - left]
            l += 1
            i += 1

        while r <= right:
            a[i] = tmp_a[r - left]
            r += 1
            i += 1
        
if __name__ == '__main__':
    #unit_test = utility_devel.Unit_Tests_Utility()
    #unit_test.get_inputs()
    #unsorted_list = unit_test.inputs[0]
    unsorted_list = [2, 5, 3, 1, 4]
    #unsorted_list = [2, 5, 3, 6, 1, 4]
    #unsorted_list = [1, 2, 3, 4, 5, 6]
    #unsorted_list = [6, 5, 4, 3, 2, 1]
    #unsorted_list = [6]
    #unsorted_list = []
    #unsorted_list = [6, 6, 6, 6, 6, 6]
    #unsorted_list = [4, 6, 4, 6, 4, 6]
    #unsorted_list = [6, 6, 6, 4, 4, 4]
    #unsorted_list = [3.81, 3.8, 3.9, 6.5, 1.99, 3.95]
    #unsorted_list = ['Hey', 'Salut', 'Azul', 'Marhaba', 'Hola']    
    
    print("Input: ", unsorted_list)

    array_merge_sort = Merge_Sort()

    array_merge_sort.merge_sort(unsorted_list)
    print("Merge Sort Output:", unsorted_list)
