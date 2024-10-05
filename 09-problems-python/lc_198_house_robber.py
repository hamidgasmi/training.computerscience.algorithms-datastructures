class Solution:
    
    # Dynamic Programming:
    # max_robbed_money(i) = Max(max_robbed_money(i - 1), max_robbed_money(i - 2) + nums[i])
    # Time Complexity: O(|nums|)
    # Space Complexity: O(1)
    def rob(self, nums: List[int]) -> int:
        
        prev_robbed_money = 0
        curr_robbed_money = 0
        for house_money in nums:
            prev_robbed_money, curr_robbed_money = curr_robbed_money, max(curr_robbed_money, prev_robbed_money + house_money)
        
        return curr_robbed_money
    
        