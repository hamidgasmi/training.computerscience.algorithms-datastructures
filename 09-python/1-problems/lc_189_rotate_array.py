class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        
        len_nums = len(nums)
        
        k %= len_nums
        if k == 0:
            return 
        
        count = 0
        start = 0
        while count < len_nums:
            
            curr = start
            prev = nums[start]
            
            while True:
                next_idx = (curr + k) % len_nums
                prev, nums[next_idx] = nums[next_idx], prev
                count += 1
                                
                curr = (curr + k) % len_nums
                
                if curr == start:
                    break
                
            start += 1