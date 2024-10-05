"""
    Let the output be product_nums
    product_nums[i] = nums[0] * ... * nums[i - 1] * nums[i + 1] * ... * nums[len(nums) - 1]
    product_nums[i] = product_left(nums from 0 to i - 1) * product_right(nums from i + 1 to len(nums) - 1)

"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def product_except_self(self, nums: List[int]) -> List[int]:
        
        len_nums = len(nums)

        assert(len_nums > 1)
        
        product_nums = [1]

        # 1. Compute the left part
        left = 1
        for i in range(1, len_nums):
            left *= nums[i - 1]
            product_nums.append(left)
        
        # 2. Compute the right part
        right = 1
        for i in range(len_nums - 2, -1, -1):
            right *= nums[i + 1]
            product_nums[i] *= right
        
        return product_nums
        