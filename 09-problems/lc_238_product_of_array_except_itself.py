# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        len_nums = len(nums)

        assert(len_nums > 1)
        
        product_nums = [1 for _ in range(len_nums)]
        
        left = 1
        for i in range(1, len_nums):
            left *= nums[i - 1]
            product_nums.append(left)
            
        right = 1
        for i in range(len_nums - 2, -1, -1):
            right *= nums[i + 1]
            product_nums[i] *= right
        
        return product_nums
        