
class Solution:

    # Solution 1: Dict
    # Time complexity: O(n)
    # Space Complexity: O(n)
    def majority_element_1(self, nums: List[int]) -> int:
        
        nums_vals = dict()
        for val in nums:
            if not val in nums_vals:
                nums_vals[val] = 0

            nums_vals[val] += 1
        
        majority_count = len(nums) // 2 + 1
        for (val, count) in nums_vals.items():
            if count >= majority_count:
                break
        
        return val

    # Solution 2: Divide and Conquer approach
    # Level    Recursion Tree   #Problem     Work                   Space
    #   0           n            1          1 * 2n          = 2n      1
    #   1        n/2 n/2         2**1       2 * 2n/2        = 2n      1
    #   2       n/4 ... n/4      2**2       2**2 * 2*n/2**2 = 2n      1
    #   ...
    #   i      n/2**i...n/2**i   2**i       2**i * 2*n/2**i = 2n      1
    #   ...
    #   logn   n/2**logn...      2**logn=n  n * 2*n/n       = 2n      1
    #   Time Complexity: O(n * logn)
    #   Space Complexity: O(logn)
    def majority_element_2(self, nums: List[int], left : int = 0, right : int = None) -> int:

        if right is None:
            right = len(nums) - 1
        
        if left > right:
            return None
        
        elif left == right:
            return nums[left]
        
        mid = (left + right) // 2
        
        left_majority = self.majority_element(nums, left, mid)
        right_majority = self.majority_element(nums, mid + 1, right)
        
        if left_majority == right_majority:
            return left_majority
        
        left_count = self._count_element(left_majority, nums, left, right)
        right_count = self._count_element(right_majority, nums, left, right)
        
        return left_majority if left_count > right_count else right_majority
    
    def _count_element(self, val, nums: List[int], left: int, right: int) -> int:
        
        count = 0
        for i in range(left, right + 1):
            if nums[i] == val:
                count += 1
        
        return count
        