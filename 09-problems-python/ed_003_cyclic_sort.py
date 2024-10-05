
"""
    1. Problem Summary / Clarifications / TDD:
        Output([3, 1, 5, 4, 2]):[1, 2, 3, 4, 5]
        Output([2, 6, 4, 3, 1, 5]):[1, 2, 3, 4, 5, 6]
        Output([1, 5, 6, 4, 3, 2]):[1, 2, 3, 4, 5, 6]

    4. Tests:
        Output([3, 1, 5, 4, 2]):[1, 2, 3, 4, 5]
        Output([2, 6, 4, 3, 1, 5]):[1, 2, 3, 4, 5, 6]
        Output([1, 5, 6, 4, 3, 2]):[1, 2, 3, 4, 5, 6]

        Edge Cases:
            Output([]):[]
            Output([1]):[1]
        
        Special Case:
            Output([1, 2, 3, 4, 5, 6]):[1, 2, 3, 4, 5, 6]

    5. Complexity Analysis:
        Time Complexity: O(n)
        Space Compexity: O(1)

"""
class Solution:

    def cyclic_sort(self, nums: [int]) -> [int]:
        
        nums_len = len(nums)
        i = 0
        while i < nums_len:
            j = nums[i] - 1

            if i == j:
                i += 1
            
            else:
                nums[j], nums[i] = nums[i], nums[j]
        
        return nums

if __name__ == '__main__':

    print(Solution().cyclic_sort([3, 1, 5, 4, 2]))
    print(Solution().cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(Solution().cyclic_sort([1, 5, 6, 4, 3, 2]))
    
    print(Solution().cyclic_sort([1, 2, 3, 4, 5, 6]))

    print(Solution().cyclic_sort([1]))
    print(Solution().cyclic_sort([]))
