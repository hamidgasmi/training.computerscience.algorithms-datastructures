"""
    1. Problem Summary / Clarifications / TDD:
        [2, 6, 10, 4, 5, 5, 8]
        [2, 6, 4, 8, 10, 9, 15]
        [2, 3, 4, 7, 5, 8, 9, 10]
        [2, 4, 5, 5, 6, 7, 8, 10]

"""
class Solution_Two_Pointers:
    """    
        2. Intuition:
            [2, 6, 4, 8, 10, 9, 15]
                ^            ^

        3. Complexity Analysis:
            Time Complexity: O(|nums|)
            Space Complexity: O(1)
                 
    """
    def find_unsorted_subarray(self, nums: List[int]) -> int:
        
        nums_len = len(nums)
        
        l, r = 0, nums_len - 1
        while (l < nums_len - 1 and nums[l] <= nums[l + 1]):
            l += 1
        if l == nums_len - 1:
            return 0
        
        while (r > 0 and nums[r] >= nums[r - 1]):
            r -= 1
        
        subarray_max = -math.inf
        subarray_min = math.inf
        for k in range(l, r + 1):
            subarray_max = max(subarray_max, nums[k])
            subarray_min = min(subarray_min, nums[k])
        
        while (l > 0 and nums[l - 1] > subarray_min):
            l -= 1
        
        while (r < nums_len - 1 and nums[r + 1] < subarray_max):
            r += 1

        return r - l + 1

class Solution_Sorting:
    """

    3. Complexity Analysis:
            Time Complexity: O(nlogn): n = |nums|
            Space Complexity: O(1) or O(n) in the worst case (according to python built-in sort function documentation)

    """
    def find_unsorted_subarray(self, nums: List[int]) -> int:
        
        sorted_nums = nums.copy()
        sorted_nums.sort()
        
        l = 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                l = i
                break
        
        r = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != sorted_nums[i]:
                r = i
                break
                
        return r - l + 1
    