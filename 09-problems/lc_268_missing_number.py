"""
    1. Problem Summary / Clarifications / TDD:
        What is the max size of the input?
        Output([3,0,1]): 2
        Output([2,0,1]): 3
        
    2. Inuition: 3 different solutions:
        - Solution 1: Math
            - missing number = sum of the arithmetic series (0, n) - sum(nums)
            - Risk: Overflow issue to compute sum of the arithmetic series (0, n)
            - The question above if relevant for this solution

        - Solution 2: Bitwise
            - xor all values from 0 to n
            - xor all values in nums

        - Solution 3: Sorting in linear space
            - if nums[i] != i, swap positions i, nums[i]

    3. Implementation:
    4. Tests:
        - Tests above
        - Edge cases:
            Output([]):  0
            Output([1]): 0
            Output([0]): 1

    5. Complexity Analysis:
        - Time Complexity: O(n)
        - Space Complexity: O(1)
    
"""
class Solution_Math:
    
    def missing_number(self, nums: List[int]) -> int:
        
        nums_len = len(nums)

        return (nums_len * (nums_len + 1)) // 2 - sum(nums)
    
class Solution_Bitwise:

    def missing_number(self, nums: List[int]) -> int:
        
        xor = 0
        for n in range(1, len(nums) + 1):
            xor ^= n
            
        for n in nums:
            xor ^= n
        
        return xor
    
class Solution_Sort:
    def missing_number(self, nums: List[int]) -> int:
        
        len_nums = len(nums)
        
        missing_number = len_nums
        
        i = 0
        while i < len_nums:
            j = nums[i]
            
            if j == len_nums:
                missing_number = i
                i += 1
            
            elif i == j:
                i += 1
                
            else:
                nums[i], nums[j] = nums[j], nums[i]
        
        return missing_number
