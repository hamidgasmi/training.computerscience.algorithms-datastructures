# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        len_nums = len(nums)
        
        product_nums = [1 for _ in range(len_nums)]
        
        product = 1
        for i in range(1, len_nums):
            product *= nums[i - 1]
            product_nums[i] *= product
            
        product = 1
        for i in range(len_nums - 2, -1, -1):
            product *= nums[i + 1]
            product_nums[i] *= product
        
        return product_nums
        