"""
    1. Problem Summary / Clarifications / TDD:
        Questions:
            - What is the maximum possible value of the array values?
            - Is it possible to have overflow issues?

        10      5,      2       6
        100      5,      2       6
        [10,3,3,7,2,9,7,4,7,2,8,6,5,1,5] 30
        [10,5,2,6] 100
        [6,5,1], 30
                
    2. Intuition:
        10      5,      2       6
        ^                           5
        ^       ^                   10 5
                ^                   5
                ^       ^           2 5
                ^               ^   2 5 6
                        ^       ^   2 6
                                ^   6       
        
"""

class Solution_Product:
    """
        Time Complexity: O(|nums| * 2) = O(|nums|)
        Space Compexity: O(1)

        Pros: Linear time solution
        Cons: Risk of overflow issues
    """

    def subarray_product_less_than_k(self, nums: List[int], k: int) -> int:
        
        len_nums = len(nums)
        
        subarr_count = 0
        subarr_product = 1
        
        l = r = 0
        while l < len_nums:
            
            while r < len_nums and subarr_product * nums[r] < k:
                
                subarr_product *= nums[r]
                r += 1
            
            if l == r:
                r += 1
                subarr_product = 1
            
            else:
                subarr_count += r - l
                subarr_product //= nums[l]
            
            l += 1
            
        return subarr_count

class Solution_Sum_of_Logarithms:
    """
        Time Complexity: O(|nums| * 2) = O(|nums|)
        Space Compexity: O(1)

        Pros: 
            - Linear time solution
            - No overflow issues
        Cons: 
            - Precision + Rounding issues
            - It's slower than the 1st. solution because of logarithm computations

    """
    def subarray_product_less_than_k(self, nums: List[int], k: int) -> int:
        if not k:
            return 0
        
        len_nums = len(nums)
        
        digits = 5
        k = round(math.log(k), digits)
        
        subarr_count = 0
        subarr_log_product = 0
        
        l = r = 0
        while l < len_nums:
            
            while r < len_nums and round(subarr_log_product + math.log(nums[r]), digits) < k:
                subarr_log_product += math.log(nums[r])
                r += 1
            
            if l == r:
                r += 1
                subarr_log_product = 0
            
            else:
                subarr_count += r - l
                subarr_log_product -= math.log(nums[l])
            
            l += 1
            
        return subarr_count